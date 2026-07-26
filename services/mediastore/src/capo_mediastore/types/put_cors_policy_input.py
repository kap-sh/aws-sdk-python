"""Generated from Smithy shape ``com.amazonaws.mediastore#PutCorsPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediastore.types.container_name
    import capo_mediastore.types.cors_policy


class PutCorsPolicyInput(TypedDict, closed=True):
    container_name: "capo_mediastore.types.container_name.ContainerName"
    """<p>The name of the container that you want to assign the CORS policy to.</p>"""
    cors_policy: "capo_mediastore.types.cors_policy.CorsPolicy"
    """<p>The CORS policy to apply to the container. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutCorsPolicyInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    import capo_mediastore.types.cors_policy

    out["CorsPolicy"] = capo_mediastore.types.cors_policy.serialize_aws_json_1_1(
        value["cors_policy"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutCorsPolicyInput:
    out: PutCorsPolicyInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("PutCorsPolicyInput.container_name required")
    if "CorsPolicy" in data:
        import capo_mediastore.types.cors_policy

        out["cors_policy"] = capo_mediastore.types.cors_policy.deserialize_aws_json_1_1(
            data["CorsPolicy"]
        )
    else:
        raise DeserializationError("PutCorsPolicyInput.cors_policy required")
    return out
