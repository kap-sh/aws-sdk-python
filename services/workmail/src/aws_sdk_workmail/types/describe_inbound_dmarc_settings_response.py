"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeInboundDmarcSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.boolean


class DescribeInboundDmarcSettingsResponse(TypedDict):
    enforced: "aws_sdk_workmail.types.boolean.Boolean"
    """<p>Lists the enforcement setting of the applied policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInboundDmarcSettingsResponse) -> dict:
    out: dict = {}
    out["Enforced"] = value.get("enforced", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInboundDmarcSettingsResponse:
    out: DescribeInboundDmarcSettingsResponse = {}  # type: ignore[typeddict-item]
    if "Enforced" in data:
        out["enforced"] = data["Enforced"]
    else:
        out["enforced"] = False
    return out
