"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#AccountSettingsDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.capacity_limits


class AccountSettingsDetail(TypedDict):
    capacity_limits: NotRequired[
        "aws_sdk_opensearchserverless.types.capacity_limits.CapacityLimits"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountSettingsDetail) -> dict:
    out: dict = {}
    if "capacity_limits" in value:
        import aws_sdk_opensearchserverless.types.capacity_limits

        out["capacityLimits"] = (
            aws_sdk_opensearchserverless.types.capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountSettingsDetail:
    out: AccountSettingsDetail = {}  # type: ignore[typeddict-item]
    if "capacityLimits" in data:
        import aws_sdk_opensearchserverless.types.capacity_limits

        out["capacity_limits"] = (
            aws_sdk_opensearchserverless.types.capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    return out
