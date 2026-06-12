"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CopyProductOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id


class CopyProductOutput(TypedDict):
    copy_product_token: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The token to use to track the progress of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyProductOutput) -> dict:
    out: dict = {}
    if "copy_product_token" in value:
        out["CopyProductToken"] = value["copy_product_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyProductOutput:
    out: CopyProductOutput = {}  # type: ignore[typeddict-item]
    if "CopyProductToken" in data:
        out["copy_product_token"] = data["CopyProductToken"]
    return out
