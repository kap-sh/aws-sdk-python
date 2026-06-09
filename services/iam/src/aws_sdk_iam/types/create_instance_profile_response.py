"""Generated from Smithy shape ``com.amazonaws.iam#CreateInstanceProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.instance_profile


class CreateInstanceProfileResponse(TypedDict):
    instance_profile: "aws_sdk_iam.types.instance_profile.InstanceProfile"
    """<p>A structure containing details about the new instance profile.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateInstanceProfileResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.instance_profile

    aws_sdk_iam.types.instance_profile.serialize_query(
        value["instance_profile"], pairs, f"{prefix}.InstanceProfile"
    )


def deserialize_query(el: Element) -> CreateInstanceProfileResponse:
    out: CreateInstanceProfileResponse = {}  # type: ignore[typeddict-item]
    child_instance_profile = el.find("InstanceProfile")
    if child_instance_profile is not None:
        import aws_sdk_iam.types.instance_profile

        out["instance_profile"] = aws_sdk_iam.types.instance_profile.deserialize_query(
            child_instance_profile
        )
    else:
        raise DeserializationError(
            "CreateInstanceProfileResponse.instance_profile required"
        )
    return out
