"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.error_code
    import aws_sdk_service_catalog.types.error_description


class RecordError(TypedDict):
    code: NotRequired["aws_sdk_service_catalog.types.error_code.ErrorCode"]
    """<p>The numeric value of the error.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.error_description.ErrorDescription"
    ]
    """<p>The description of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordError) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordError:
    out: RecordError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
