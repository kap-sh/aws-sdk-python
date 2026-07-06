"""Generated from Smithy shape ``com.amazonaws.ssm#GetOpsItemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item


class GetOpsItemResponse(TypedDict, closed=True):
    ops_item: NotRequired["aws_sdk_ssm.types.ops_item.OpsItem"]
    """<p>The OpsItem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpsItemResponse) -> dict:
    out: dict = {}
    if "ops_item" in value:
        import aws_sdk_ssm.types.ops_item

        out["OpsItem"] = aws_sdk_ssm.types.ops_item.serialize_aws_json_1_1(
            value["ops_item"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpsItemResponse:
    out: GetOpsItemResponse = {}  # type: ignore[typeddict-item]
    if "OpsItem" in data:
        import aws_sdk_ssm.types.ops_item

        out["ops_item"] = aws_sdk_ssm.types.ops_item.deserialize_aws_json_1_1(
            data["OpsItem"]
        )
    return out
