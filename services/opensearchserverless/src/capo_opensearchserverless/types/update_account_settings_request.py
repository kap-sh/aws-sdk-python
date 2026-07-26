"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateAccountSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.capacity_limits


class UpdateAccountSettingsRequest(TypedDict, closed=True):
    capacity_limits: NotRequired[
        "capo_opensearchserverless.types.capacity_limits.CapacityLimits"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAccountSettingsRequest) -> dict:
    out: dict = {}
    if "capacity_limits" in value:
        import capo_opensearchserverless.types.capacity_limits

        out["capacityLimits"] = (
            capo_opensearchserverless.types.capacity_limits.serialize_aws_json_1_0(
                value["capacity_limits"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAccountSettingsRequest:
    out: UpdateAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    if "capacityLimits" in data:
        import capo_opensearchserverless.types.capacity_limits

        out["capacity_limits"] = (
            capo_opensearchserverless.types.capacity_limits.deserialize_aws_json_1_0(
                data["capacityLimits"]
            )
        )
    return out
