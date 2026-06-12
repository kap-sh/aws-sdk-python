"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeServiceActionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.service_action_detail


class DescribeServiceActionOutput(TypedDict):
    service_action_detail: NotRequired[
        "aws_sdk_service_catalog.types.service_action_detail.ServiceActionDetail"
    ]
    """<p>Detailed information about the self-service action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceActionOutput) -> dict:
    out: dict = {}
    if "service_action_detail" in value:
        import aws_sdk_service_catalog.types.service_action_detail

        out["ServiceActionDetail"] = (
            aws_sdk_service_catalog.types.service_action_detail.serialize_aws_json_1_1(
                value["service_action_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceActionOutput:
    out: DescribeServiceActionOutput = {}  # type: ignore[typeddict-item]
    if "ServiceActionDetail" in data:
        import aws_sdk_service_catalog.types.service_action_detail

        out["service_action_detail"] = (
            aws_sdk_service_catalog.types.service_action_detail.deserialize_aws_json_1_1(
                data["ServiceActionDetail"]
            )
        )
    return out
