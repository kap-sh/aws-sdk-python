"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.age_range
    import aws_sdk_rekognition.types.beard
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.emotions
    import aws_sdk_rekognition.types.eye_direction
    import aws_sdk_rekognition.types.eye_open
    import aws_sdk_rekognition.types.eyeglasses
    import aws_sdk_rekognition.types.face_occluded
    import aws_sdk_rekognition.types.gender
    import aws_sdk_rekognition.types.image_quality
    import aws_sdk_rekognition.types.landmarks
    import aws_sdk_rekognition.types.mouth_open
    import aws_sdk_rekognition.types.mustache
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.pose
    import aws_sdk_rekognition.types.smile
    import aws_sdk_rekognition.types.sunglasses


class FaceDetail(TypedDict, closed=True):
    bounding_box: NotRequired["aws_sdk_rekognition.types.bounding_box.BoundingBox"]
    """<p>Bounding box of the face. Default attribute.</p>"""
    age_range: NotRequired["aws_sdk_rekognition.types.age_range.AgeRange"]
    """<p>The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.</p>"""
    smile: NotRequired["aws_sdk_rekognition.types.smile.Smile"]
    """<p>Indicates whether or not the face is smiling, and the confidence level in the determination.</p>"""
    eyeglasses: NotRequired["aws_sdk_rekognition.types.eyeglasses.Eyeglasses"]
    """<p>Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.</p>"""
    sunglasses: NotRequired["aws_sdk_rekognition.types.sunglasses.Sunglasses"]
    """<p>Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.</p>"""
    gender: NotRequired["aws_sdk_rekognition.types.gender.Gender"]
    """<p>The predicted gender of a detected face. </p>"""
    beard: NotRequired["aws_sdk_rekognition.types.beard.Beard"]
    """<p>Indicates whether or not the face has a beard, and the confidence level in the determination.</p>"""
    mustache: NotRequired["aws_sdk_rekognition.types.mustache.Mustache"]
    """<p>Indicates whether or not the face has a mustache, and the confidence level in the determination.</p>"""
    eyes_open: NotRequired["aws_sdk_rekognition.types.eye_open.EyeOpen"]
    """<p>Indicates whether or not the eyes on the face are open, and the confidence level in the determination.</p>"""
    mouth_open: NotRequired["aws_sdk_rekognition.types.mouth_open.MouthOpen"]
    """<p>Indicates whether or not the mouth on the face is open, and the confidence level in the determination.</p>"""
    emotions: NotRequired["aws_sdk_rekognition.types.emotions.Emotions"]
    """<p>The emotions that appear to be expressed on the face, and the confidence level in the determination. The API is only making a determination of the physical appearance of a person's face. It is not a determination of the person’s internal emotional state and should not be used in such a way. For example, a person pretending to have a sad face might not be sad emotionally.</p>"""
    landmarks: NotRequired["aws_sdk_rekognition.types.landmarks.Landmarks"]
    """<p>Indicates the location of landmarks on the face. Default attribute.</p>"""
    pose: NotRequired["aws_sdk_rekognition.types.pose.Pose"]
    """<p>Indicates the pose of the face as determined by its pitch, roll, and yaw. Default attribute.</p>"""
    quality: NotRequired["aws_sdk_rekognition.types.image_quality.ImageQuality"]
    """<p>Identifies image brightness and sharpness. Default attribute.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>Confidence level that the bounding box contains a face (and not a different object such as a tree). Default attribute.</p>"""
    face_occluded: NotRequired["aws_sdk_rekognition.types.face_occluded.FaceOccluded"]
    r"""<p> <code>FaceOccluded</code> should return \"true\" with a high confidence score if a detected face’s eyes, nose, and mouth are partially captured or if they are covered by masks, dark sunglasses, cell phones, hands, or other objects. <code>FaceOccluded</code> should return \"false\" with a high confidence score if common occurrences that do not impact face verification are detected, such as eye glasses, lightly tinted sunglasses, strands of hair, and others. </p>"""
    eye_direction: NotRequired["aws_sdk_rekognition.types.eye_direction.EyeDirection"]
    """<p>Indicates the direction the eyes are gazing in, as defined by pitch and yaw.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceDetail) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import aws_sdk_rekognition.types.bounding_box

        out["BoundingBox"] = (
            aws_sdk_rekognition.types.bounding_box.serialize_aws_json_1_1(
                value["bounding_box"]
            )
        )
    if "age_range" in value:
        import aws_sdk_rekognition.types.age_range

        out["AgeRange"] = aws_sdk_rekognition.types.age_range.serialize_aws_json_1_1(
            value["age_range"]
        )
    if "smile" in value:
        import aws_sdk_rekognition.types.smile

        out["Smile"] = aws_sdk_rekognition.types.smile.serialize_aws_json_1_1(
            value["smile"]
        )
    if "eyeglasses" in value:
        import aws_sdk_rekognition.types.eyeglasses

        out["Eyeglasses"] = aws_sdk_rekognition.types.eyeglasses.serialize_aws_json_1_1(
            value["eyeglasses"]
        )
    if "sunglasses" in value:
        import aws_sdk_rekognition.types.sunglasses

        out["Sunglasses"] = aws_sdk_rekognition.types.sunglasses.serialize_aws_json_1_1(
            value["sunglasses"]
        )
    if "gender" in value:
        import aws_sdk_rekognition.types.gender

        out["Gender"] = aws_sdk_rekognition.types.gender.serialize_aws_json_1_1(
            value["gender"]
        )
    if "beard" in value:
        import aws_sdk_rekognition.types.beard

        out["Beard"] = aws_sdk_rekognition.types.beard.serialize_aws_json_1_1(
            value["beard"]
        )
    if "mustache" in value:
        import aws_sdk_rekognition.types.mustache

        out["Mustache"] = aws_sdk_rekognition.types.mustache.serialize_aws_json_1_1(
            value["mustache"]
        )
    if "eyes_open" in value:
        import aws_sdk_rekognition.types.eye_open

        out["EyesOpen"] = aws_sdk_rekognition.types.eye_open.serialize_aws_json_1_1(
            value["eyes_open"]
        )
    if "mouth_open" in value:
        import aws_sdk_rekognition.types.mouth_open

        out["MouthOpen"] = aws_sdk_rekognition.types.mouth_open.serialize_aws_json_1_1(
            value["mouth_open"]
        )
    if "emotions" in value:
        import aws_sdk_rekognition.types.emotions

        out["Emotions"] = aws_sdk_rekognition.types.emotions.serialize_aws_json_1_1(
            value["emotions"]
        )
    if "landmarks" in value:
        import aws_sdk_rekognition.types.landmarks

        out["Landmarks"] = aws_sdk_rekognition.types.landmarks.serialize_aws_json_1_1(
            value["landmarks"]
        )
    if "pose" in value:
        import aws_sdk_rekognition.types.pose

        out["Pose"] = aws_sdk_rekognition.types.pose.serialize_aws_json_1_1(
            value["pose"]
        )
    if "quality" in value:
        import aws_sdk_rekognition.types.image_quality

        out["Quality"] = aws_sdk_rekognition.types.image_quality.serialize_aws_json_1_1(
            value["quality"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "face_occluded" in value:
        import aws_sdk_rekognition.types.face_occluded

        out["FaceOccluded"] = (
            aws_sdk_rekognition.types.face_occluded.serialize_aws_json_1_1(
                value["face_occluded"]
            )
        )
    if "eye_direction" in value:
        import aws_sdk_rekognition.types.eye_direction

        out["EyeDirection"] = (
            aws_sdk_rekognition.types.eye_direction.serialize_aws_json_1_1(
                value["eye_direction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FaceDetail:
    out: FaceDetail = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import aws_sdk_rekognition.types.bounding_box

        out["bounding_box"] = (
            aws_sdk_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "AgeRange" in data:
        import aws_sdk_rekognition.types.age_range

        out["age_range"] = aws_sdk_rekognition.types.age_range.deserialize_aws_json_1_1(
            data["AgeRange"]
        )
    if "Smile" in data:
        import aws_sdk_rekognition.types.smile

        out["smile"] = aws_sdk_rekognition.types.smile.deserialize_aws_json_1_1(
            data["Smile"]
        )
    if "Eyeglasses" in data:
        import aws_sdk_rekognition.types.eyeglasses

        out["eyeglasses"] = (
            aws_sdk_rekognition.types.eyeglasses.deserialize_aws_json_1_1(
                data["Eyeglasses"]
            )
        )
    if "Sunglasses" in data:
        import aws_sdk_rekognition.types.sunglasses

        out["sunglasses"] = (
            aws_sdk_rekognition.types.sunglasses.deserialize_aws_json_1_1(
                data["Sunglasses"]
            )
        )
    if "Gender" in data:
        import aws_sdk_rekognition.types.gender

        out["gender"] = aws_sdk_rekognition.types.gender.deserialize_aws_json_1_1(
            data["Gender"]
        )
    if "Beard" in data:
        import aws_sdk_rekognition.types.beard

        out["beard"] = aws_sdk_rekognition.types.beard.deserialize_aws_json_1_1(
            data["Beard"]
        )
    if "Mustache" in data:
        import aws_sdk_rekognition.types.mustache

        out["mustache"] = aws_sdk_rekognition.types.mustache.deserialize_aws_json_1_1(
            data["Mustache"]
        )
    if "EyesOpen" in data:
        import aws_sdk_rekognition.types.eye_open

        out["eyes_open"] = aws_sdk_rekognition.types.eye_open.deserialize_aws_json_1_1(
            data["EyesOpen"]
        )
    if "MouthOpen" in data:
        import aws_sdk_rekognition.types.mouth_open

        out["mouth_open"] = (
            aws_sdk_rekognition.types.mouth_open.deserialize_aws_json_1_1(
                data["MouthOpen"]
            )
        )
    if "Emotions" in data:
        import aws_sdk_rekognition.types.emotions

        out["emotions"] = aws_sdk_rekognition.types.emotions.deserialize_aws_json_1_1(
            data["Emotions"]
        )
    if "Landmarks" in data:
        import aws_sdk_rekognition.types.landmarks

        out["landmarks"] = aws_sdk_rekognition.types.landmarks.deserialize_aws_json_1_1(
            data["Landmarks"]
        )
    if "Pose" in data:
        import aws_sdk_rekognition.types.pose

        out["pose"] = aws_sdk_rekognition.types.pose.deserialize_aws_json_1_1(
            data["Pose"]
        )
    if "Quality" in data:
        import aws_sdk_rekognition.types.image_quality

        out["quality"] = (
            aws_sdk_rekognition.types.image_quality.deserialize_aws_json_1_1(
                data["Quality"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "FaceOccluded" in data:
        import aws_sdk_rekognition.types.face_occluded

        out["face_occluded"] = (
            aws_sdk_rekognition.types.face_occluded.deserialize_aws_json_1_1(
                data["FaceOccluded"]
            )
        )
    if "EyeDirection" in data:
        import aws_sdk_rekognition.types.eye_direction

        out["eye_direction"] = (
            aws_sdk_rekognition.types.eye_direction.deserialize_aws_json_1_1(
                data["EyeDirection"]
            )
        )
    return out
