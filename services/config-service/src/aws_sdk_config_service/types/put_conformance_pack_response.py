"""Generated from Smithy shape ``com.amazonaws.configservice#PutConformancePackResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_arn


class PutConformancePackResponse(TypedDict):
    conformance_pack_arn: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_arn.ConformancePackArn"
    ]
    """<p>ARN of the conformance pack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConformancePackResponse) -> dict:
    out: dict = {}
    if "conformance_pack_arn" in value:
        out["ConformancePackArn"] = value["conformance_pack_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConformancePackResponse:
    out: PutConformancePackResponse = {}  # type: ignore[typeddict-item]
    if "ConformancePackArn" in data:
        out["conformance_pack_arn"] = data["ConformancePackArn"]
    return out
