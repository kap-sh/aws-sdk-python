"""Generated from Smithy shape ``com.amazonaws.iam#PolicyRoleListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy_role

PolicyRoleListType: TypeAlias = list["aws_sdk_iam.types.policy_role.PolicyRole"]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyRoleListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.policy_role

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.policy_role.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PolicyRoleListType:
    import aws_sdk_iam.types.policy_role

    out: PolicyRoleListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.policy_role.deserialize_query(child))
    return out


def serialize_query_flat(
    value: PolicyRoleListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.policy_role

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.policy_role.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> PolicyRoleListType:
    import aws_sdk_iam.types.policy_role

    out: PolicyRoleListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.policy_role.deserialize_query(child))
    return out
