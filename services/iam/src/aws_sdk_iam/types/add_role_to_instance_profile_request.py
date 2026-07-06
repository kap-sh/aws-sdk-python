"""Generated from Smithy shape ``com.amazonaws.iam#AddRoleToInstanceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.instance_profile_name_type
    import aws_sdk_iam.types.role_name_type


class AddRoleToInstanceProfileRequest(TypedDict, closed=True):
    instance_profile_name: (
        "aws_sdk_iam.types.instance_profile_name_type.instanceProfileNameType"
    )
    r"""<p>The name of the instance profile to update.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    role_name: "aws_sdk_iam.types.role_name_type.roleNameType"
    r"""<p>The name of the role to add.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddRoleToInstanceProfileRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.InstanceProfileName", str(value["instance_profile_name"])))
    pairs.append((f"{prefix}.RoleName", str(value["role_name"])))


def deserialize_query(el: Element) -> AddRoleToInstanceProfileRequest:
    out: AddRoleToInstanceProfileRequest = {}  # type: ignore[typeddict-item]
    child_instance_profile_name = el.find("InstanceProfileName")
    if child_instance_profile_name is not None:
        out["instance_profile_name"] = str(child_instance_profile_name.text or "")
    else:
        raise DeserializationError(
            "AddRoleToInstanceProfileRequest.instance_profile_name required"
        )
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError("AddRoleToInstanceProfileRequest.role_name required")
    return out
