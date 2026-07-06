"""Generated from Smithy shape ``com.amazonaws.translate#GetTerminologyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.resource_name
    import aws_sdk_translate.types.terminology_data_format


class GetTerminologyRequest(TypedDict, closed=True):
    name: "aws_sdk_translate.types.resource_name.ResourceName"
    """<p>The name of the custom terminology being retrieved.</p>"""
    terminology_data_format: NotRequired[
        "aws_sdk_translate.types.terminology_data_format.TerminologyDataFormat"
    ]
    """<p>The data format of the custom terminology being retrieved.</p> <p>If you don't specify this parameter, Amazon Translate returns a file with the same format as the file that was imported to create the terminology. </p> <p>If you specify this parameter when you retrieve a multi-directional terminology resource, you must specify the same format as the input file that was imported to create it. Otherwise, Amazon Translate throws an error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTerminologyRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "terminology_data_format" in value:
        import aws_sdk_translate.types.terminology_data_format

        out["TerminologyDataFormat"] = (
            aws_sdk_translate.types.terminology_data_format.serialize_aws_json_1_1(
                value["terminology_data_format"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTerminologyRequest:
    out: GetTerminologyRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetTerminologyRequest.name required")
    if "TerminologyDataFormat" in data:
        import aws_sdk_translate.types.terminology_data_format

        out["terminology_data_format"] = (
            aws_sdk_translate.types.terminology_data_format.deserialize_aws_json_1_1(
                data["TerminologyDataFormat"]
            )
        )
    return out
