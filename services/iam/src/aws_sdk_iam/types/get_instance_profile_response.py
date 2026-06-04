"""Generated from Smithy shape ``com.amazonaws.iam#GetInstanceProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.instance_profile


class GetInstanceProfileResponse(TypedDict):
    instance_profile: "aws_sdk_iam.types.instance_profile.InstanceProfile"
    """<p>A structure containing details about the instance profile.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetInstanceProfileResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.instance_profile

    aws_sdk_iam.types.instance_profile.serialize_query(
        value["instance_profile"], pairs, f"{prefix}.InstanceProfile"
    )


def deserialize_query(el: Element) -> GetInstanceProfileResponse:
    out: GetInstanceProfileResponse = {}  # type: ignore[typeddict-item]
    child_instance_profile = el.find("InstanceProfile")
    if child_instance_profile is not None:
        import aws_sdk_iam.types.instance_profile

        out["instance_profile"] = aws_sdk_iam.types.instance_profile.deserialize_query(
            child_instance_profile
        )
    else:
        raise DeserializationError(
            "GetInstanceProfileResponse.instance_profile required"
        )
    return out
