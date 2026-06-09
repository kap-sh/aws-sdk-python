"""Generated from Smithy shape ``com.amazonaws.iam#DeleteInstanceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.instance_profile_name_type


class DeleteInstanceProfileRequest(TypedDict):
    instance_profile_name: (
        "aws_sdk_iam.types.instance_profile_name_type.instanceProfileNameType"
    )
    """<p>The name of the instance profile to delete.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteInstanceProfileRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.InstanceProfileName", str(value["instance_profile_name"])))


def deserialize_query(el: Element) -> DeleteInstanceProfileRequest:
    out: DeleteInstanceProfileRequest = {}  # type: ignore[typeddict-item]
    child_instance_profile_name = el.find("InstanceProfileName")
    if child_instance_profile_name is not None:
        out["instance_profile_name"] = str(child_instance_profile_name.text or "")
    else:
        raise DeserializationError(
            "DeleteInstanceProfileRequest.instance_profile_name required"
        )
    return out
