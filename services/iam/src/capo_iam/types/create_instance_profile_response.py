"""Generated from Smithy shape ``com.amazonaws.iam#CreateInstanceProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.instance_profile


class CreateInstanceProfileResponse(TypedDict, closed=True):
    instance_profile: "capo_iam.types.instance_profile.InstanceProfile"
    """<p>A structure containing details about the new instance profile.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateInstanceProfileResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.instance_profile

    capo_iam.types.instance_profile.serialize_query(
        value["instance_profile"], pairs, f"{key_prefix}InstanceProfile"
    )


def deserialize_query(el: Element) -> CreateInstanceProfileResponse:
    out: CreateInstanceProfileResponse = {}  # type: ignore[typeddict-item]
    child_instance_profile = el.find("InstanceProfile")
    if child_instance_profile is not None:
        import capo_iam.types.instance_profile

        out["instance_profile"] = capo_iam.types.instance_profile.deserialize_query(
            child_instance_profile
        )
    else:
        raise DeserializationError(
            "CreateInstanceProfileResponse.instance_profile required"
        )
    return out
