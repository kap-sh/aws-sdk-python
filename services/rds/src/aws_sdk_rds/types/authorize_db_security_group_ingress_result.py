"""Generated from Smithy shape ``com.amazonaws.rds#AuthorizeDBSecurityGroupIngressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_security_group


class AuthorizeDBSecurityGroupIngressResult(TypedDict, closed=True):
    db_security_group: NotRequired[
        "aws_sdk_rds.types.db_security_group.DBSecurityGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizeDBSecurityGroupIngressResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_security_group" in value:
        import aws_sdk_rds.types.db_security_group

        aws_sdk_rds.types.db_security_group.serialize_query(
            value["db_security_group"], pairs, f"{prefix}.DBSecurityGroup"
        )


def deserialize_query(el: Element) -> AuthorizeDBSecurityGroupIngressResult:
    out: AuthorizeDBSecurityGroupIngressResult = {}  # type: ignore[typeddict-item]
    child_db_security_group = el.find("DBSecurityGroup")
    if child_db_security_group is not None:
        import aws_sdk_rds.types.db_security_group

        out["db_security_group"] = (
            aws_sdk_rds.types.db_security_group.deserialize_query(
                child_db_security_group
            )
        )
    return out
