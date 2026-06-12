"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.description
    import aws_sdk_service_catalog.types.output_key
    import aws_sdk_service_catalog.types.output_value


class RecordOutput(TypedDict):
    output_key: NotRequired["aws_sdk_service_catalog.types.output_key.OutputKey"]
    """<p>The output key.</p>"""
    output_value: NotRequired["aws_sdk_service_catalog.types.output_value.OutputValue"]
    """<p>The output value.</p>"""
    description: NotRequired["aws_sdk_service_catalog.types.description.Description"]
    """<p>The description of the output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordOutput) -> dict:
    out: dict = {}
    if "output_key" in value:
        out["OutputKey"] = value["output_key"]
    if "output_value" in value:
        out["OutputValue"] = value["output_value"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordOutput:
    out: RecordOutput = {}  # type: ignore[typeddict-item]
    if "OutputKey" in data:
        out["output_key"] = data["OutputKey"]
    if "OutputValue" in data:
        out["output_value"] = data["OutputValue"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
