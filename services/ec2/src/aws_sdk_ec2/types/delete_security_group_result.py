"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSecurityGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.security_group_id

DeleteSecurityGroupResult = TypedDict(
    "DeleteSecurityGroupResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
        "group_id": NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteSecurityGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "return" in value:
        pairs.append((f"{prefix}.Return", "true" if value["return"] else "false"))
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))


def deserialize_ec2_query(el: Element) -> DeleteSecurityGroupResult:
    out: DeleteSecurityGroupResult = {}  # type: ignore[typeddict-item]
    child_return = el.find("Return")
    if child_return is not None:
        out["return"] = (child_return.text or "").lower() == "true"
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    return out
