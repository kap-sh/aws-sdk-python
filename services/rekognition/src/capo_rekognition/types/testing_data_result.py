"""Generated from Smithy shape ``com.amazonaws.rekognition#TestingDataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.testing_data
    import capo_rekognition.types.validation_data


class TestingDataResult(TypedDict, closed=True):
    input: NotRequired["capo_rekognition.types.testing_data.TestingData"]
    """<p>The testing dataset that was supplied for training.</p>"""
    output: NotRequired["capo_rekognition.types.testing_data.TestingData"]
    """<p>The subset of the dataset that was actually tested. Some images (assets) might not be tested due to file formatting and other issues. </p>"""
    validation: NotRequired["capo_rekognition.types.validation_data.ValidationData"]
    """<p>The location of the data validation manifest. The data validation manifest is created for the test dataset during model training.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestingDataResult) -> dict:
    out: dict = {}
    if "input" in value:
        import capo_rekognition.types.testing_data

        out["Input"] = capo_rekognition.types.testing_data.serialize_aws_json_1_1(
            value["input"]
        )
    if "output" in value:
        import capo_rekognition.types.testing_data

        out["Output"] = capo_rekognition.types.testing_data.serialize_aws_json_1_1(
            value["output"]
        )
    if "validation" in value:
        import capo_rekognition.types.validation_data

        out["Validation"] = (
            capo_rekognition.types.validation_data.serialize_aws_json_1_1(
                value["validation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestingDataResult:
    out: TestingDataResult = {}  # type: ignore[typeddict-item]
    if "Input" in data:
        import capo_rekognition.types.testing_data

        out["input"] = capo_rekognition.types.testing_data.deserialize_aws_json_1_1(
            data["Input"]
        )
    if "Output" in data:
        import capo_rekognition.types.testing_data

        out["output"] = capo_rekognition.types.testing_data.deserialize_aws_json_1_1(
            data["Output"]
        )
    if "Validation" in data:
        import capo_rekognition.types.validation_data

        out["validation"] = (
            capo_rekognition.types.validation_data.deserialize_aws_json_1_1(
                data["Validation"]
            )
        )
    return out
