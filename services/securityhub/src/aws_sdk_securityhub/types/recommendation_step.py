"""Generated from Smithy shape ``com.amazonaws.securityhub#RecommendationStep``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.unused_permissions_recommendation_step


class _RecommendationStep_UnusedPermissions(TypedDict):
    UnusedPermissions: "aws_sdk_securityhub.types.unused_permissions_recommendation_step.UnusedPermissionsRecommendationStep"


RecommendationStep: TypeAlias = _RecommendationStep_UnusedPermissions


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStep) -> dict:
    if "UnusedPermissions" in value:
        import aws_sdk_securityhub.types.unused_permissions_recommendation_step

        return {
            "UnusedPermissions": aws_sdk_securityhub.types.unused_permissions_recommendation_step.serialize_json(
                value["UnusedPermissions"]
            )
        }
    else:
        raise SerializationError("RecommendationStep: no variant present")


def deserialize_json(data: dict) -> RecommendationStep:
    if "UnusedPermissions" in data:
        import aws_sdk_securityhub.types.unused_permissions_recommendation_step

        return {
            "UnusedPermissions": aws_sdk_securityhub.types.unused_permissions_recommendation_step.deserialize_json(
                data["UnusedPermissions"]
            )
        }
    else:
        raise DeserializationError("RecommendationStep: no recognized variant key")
