from unittest import TestCase
from prompts import GenerateScenesPrompt
from api import SDAPI
import base64
from PIL import Image
import io
import PIL
import base64
from dotenv import load_dotenv
load_dotenv()

class TestGenerateSceneImage(TestCase):
    def test_empty(self):
        prompt = "Girl and elephant, (young girl in a bright green lehenga (sitting cross-legged:1.2)), (Indian elephant (looking at Geetha with large, worried eyes)), (Thick Forest with a tangle of thorny bushes, suspenseful shadows filtering through the trees), (Kids illustration, Pixar style:1.2), masterpiece, sharp focus, highly detailed, cartoon"
        
        
        with open("tests/prompts/Generate_scene/canny_image.png", "rb") as f:
            conditioned_image = f.read()
            conditioned_image = base64.b64encode(conditioned_image).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/Geetha_kneeling.png", "rb") as f:
            first_ref_img = f.read()
            first_ref_img = base64.b64encode(first_ref_img).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/ananda_relieved.png", "rb") as f:
            second_ref_img = f.read()
            second_ref_img = base64.b64encode(second_ref_img).decode("utf-8")
       
        image_data = SDAPI.reference_image(conditioned_image=conditioned_image,first_ref_image=first_ref_img,second_ref_image=second_ref_img, prompt=prompt, seed=0, steps=40)
 
        img_data = base64.b64decode(image_data)
        with open(f"final_scene_testing.png", "wb") as f:
            f.write(img_data)
            
    # test on first scene prompt generated by final scene LLM prompt
    def test_first_scene(self):
        prompt = "Bala and Simba, (young boy in shorts and a t-shirt (running joyfully, wide smile, eyes focused on Simba:1.2)), (golden-furred dog (bounding after waves, tail high and wagging, looks playful:1.2)), (Marina Beach under bright skies, kite-flyers in background, Chennai skyline in distance, vendors and families on shore), (Kids illustration, Pixar style:1.2), masterpiece, sharp focus, highly detailed, cartoon"
        
        
        with open("tests/prompts/Generate_scene/canny_bb_scene0.png", "rb") as f:
            conditioned_image = f.read()
            conditioned_image = base64.b64encode(conditioned_image).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/bala_pose_one.png", "rb") as f:
            first_ref_img = f.read()
            first_ref_img = base64.b64encode(first_ref_img).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/simba_pose_one.png", "rb") as f:
            second_ref_img = f.read()
            second_ref_img = base64.b64encode(second_ref_img).decode("utf-8")
       
        image_data = SDAPI.reference_image(conditioned_image=conditioned_image,first_ref_image=first_ref_img,second_ref_image=second_ref_img, prompt=prompt, seed=0, steps=40)
 
        img_data = base64.b64decode(image_data)
        with open(f"final_scene0_image.png", "wb") as f:
            f.write(img_data)
            
            
    def test_final_scene_generation(self):
        prompt = "Bala and Simba, (boy in bright yellow T-shirt, navy blue shorts, (walking energetically:1.2), (bright smile:1.2)), (Golden Retriever with cream-colored coat, (playfully tugging on leash:1.2), (curious expression, wide eyes:1.2)), (Marina Beach with ocean backdrop, colorful umbrellas, vendor-filled golden sandy beach, families in the sun), (Kids illustration, Pixar style:1.2), masterpiece, sharp focus, highly detailed, cartoon"
        
        
        with open("tests/prompts/Generate_scene/inputs/scene3_bounding_box.png", "rb") as f:
            conditioned_image = f.read()
            conditioned_image = base64.b64encode(conditioned_image).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/inputs/scene0_Bala.png", "rb") as f:
            first_ref_img = f.read()
            first_ref_img = base64.b64encode(first_ref_img).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/inputs/scene0_Simba.png", "rb") as f:
            second_ref_img = f.read()
            second_ref_img = base64.b64encode(second_ref_img).decode("utf-8")
       
        image_data = SDAPI.reference_image(conditioned_image=conditioned_image,first_ref_image=first_ref_img,second_ref_image=second_ref_img, prompt=prompt, seed=0, steps=40)
 
        img_data = base64.b64decode(image_data)
        with open(f"tests/prompts/Generate_scene/outputs/final_scene_manual.png", "wb") as f:
            f.write(img_data)
            
    def test_object_detection(self):
        prompt = "Bala and Simba, (young boy in a vibrant, traditional Tamil lungi, knotted at the waist and paired with a plain white shirt (running joyfully, wide smile:1.2)), (golden-furred dog (bounding after waves, tail high and wagging, looks playful:1.2)), (Marina Beach bustling with kite-flyers, bright skies, distant Chennai skyline, vendors and families along the shore), (Kids illustration, Pixar style:1.2), masterpiece, sharp focus, highly detailed, cartoon"
        
        with open("tests/prompts/Generate_scene/inputs/object_detection_bb.png", "rb") as f:
            conditioned_image = f.read()
            conditioned_image = base64.b64encode(conditioned_image).decode("utf-8")
       
        with open("tests/prompts/Bounding_box/object_detection/inputs/Bala_bb.png", "rb") as f:
            first_ref_img = f.read()
            first_ref_img = base64.b64encode(first_ref_img).decode("utf-8")
       
        with open("tests/prompts/Bounding_box/object_detection/inputs/Simba_bb.png", "rb") as f:
            second_ref_img = f.read()
            second_ref_img = base64.b64encode(second_ref_img).decode("utf-8")
       
        image_data = SDAPI.reference_image(conditioned_image=conditioned_image,first_ref_image=first_ref_img,second_ref_image=second_ref_img, prompt=prompt, seed=0, steps=40)
 
        img_data = base64.b64decode(image_data)
        with open(f"tests/prompts/Generate_scene/outputs/object_detection_final_scene.png", "wb") as f:
            f.write(img_data)
        
    def test_new_case(self):
        prompt = "Bala and Simba, (young boy in a vibrant t-shirt and shorts, (running with wide open arms and a big smile:1.2)), (playful pup with tongue lolling out, (tail wagging, looking up at Bala with excited eyes:1.2)), (Expansive Marina Beach, crowded with families, colorful food stalls, iconic lighthouse casting a tall shadow, wavy palm trees), (Kids illustration, Pixar style:1.2), masterpiece, sharp focus, highly detailed, cartoon"
        
        with open("tests/prompts/Generate_scene/inputs/reference_image_scene10.png", "rb") as f:
            conditioned_image = f.read()
            conditioned_image = base64.b64encode(conditioned_image).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/inputs/scene_10_bounding_box.png", "rb") as f:
            first_ref_img = f.read()
            first_ref_img = base64.b64encode(first_ref_img).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/inputs/scene_10_bounding_box.png", "rb") as f:
            second_ref_img = f.read()
            second_ref_img = base64.b64encode(second_ref_img).decode("utf-8")    
            
        image_data = SDAPI.reference_image(conditioned_image=conditioned_image,first_ref_image=first_ref_img,second_ref_image=second_ref_img, prompt=prompt, seed=0, steps=40)
 
        img_data = base64.b64decode(image_data)
        with open(f"tests/prompts/Generate_scene/outputs/final_scene_10.png", "wb") as f:
            f.write(img_data)
            
    def test_only_action(self):
        prompt = "Bala and Simba, (young boy in a traditional South Indian half-sleeve shirt and shorts (running excitedly towards the sea with a big smile:1.2)), (golden retriever (matching Bala's pace with tongue out and tail wagging:1.2)), (Marina Beach with sunrise over the ocean, Chennai cityscape in the distance, colorful kites in the sky, South Indian stalls with architectural motifs), (Kids illustration, Pixar style:1.2), masterpiece, sharp focus, highly detailed, cartoon"
        
        with open("tests/prompts/Generate_scene/inputs/reference_image_scene0.png", "rb") as f:
            conditioned_image = f.read()
            conditioned_image = base64.b64encode(conditioned_image).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/inputs/scene0_character_Bala.png", "rb") as f:
            first_ref_img = f.read()
            first_ref_img = base64.b64encode(first_ref_img).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/inputs/scene0_character_Simba.png", "rb") as f:
            second_ref_img = f.read()
            second_ref_img = base64.b64encode(second_ref_img).decode("utf-8")    
            
        image_data = SDAPI.reference_image(conditioned_image=conditioned_image,first_ref_image=first_ref_img,second_ref_image=second_ref_img, prompt=prompt, seed=0, steps=40)
 
        img_data = base64.b64decode(image_data)
        with open(f"tests/prompts/Generate_scene/outputs/final_scene_only_action.png", "wb") as f:
            f.write(img_data)
     
            
    def test_both_desc_action(self):
        prompt = "Bala and Simba, ((boy in a bright yellow cotton T-shirt and navy blue shorts:1.5), (running excitedly, a big smile, short curly hair bouncing:1.2)), ((golden-furred dog with red collar:1.5), (running with tongue out, tail wagging, alert ears:1.2)), (Marina Beach at sunrise, panoramic ocean view, Chennai cityscape, sand with colorful kites, iconic palm trees, South Indian stalls with architectural motifs), (Kids illustration, Pixar style:1.2), masterpiece, sharp focus, highly detailed, cartoon"
        
        with open("tests/prompts/Generate_scene/inputs/reference_image_scene0.png", "rb") as f:
            conditioned_image = f.read()
            conditioned_image = base64.b64encode(conditioned_image).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/inputs/scene0_character_Bala.png", "rb") as f:
            first_ref_img = f.read()
            first_ref_img = base64.b64encode(first_ref_img).decode("utf-8")
       
        with open("tests/prompts/Generate_scene/inputs/scene0_character_Simba.png", "rb") as f:
            second_ref_img = f.read()
            second_ref_img = base64.b64encode(second_ref_img).decode("utf-8")    
            
        image_data = SDAPI.reference_image(conditioned_image=conditioned_image,first_ref_image=first_ref_img,second_ref_image=second_ref_img, prompt=prompt)
 
        img_data = base64.b64decode(image_data)
        with open(f"tests/prompts/Generate_scene/outputs/final_scene_desc_action.png", "wb") as f:
            f.write(img_data)    