"""Generated from Smithy shape ``com.amazonaws.rds#RevokeDBSecurityGroupIngressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_security_group


class RevokeDBSecurityGroupIngressResult(TypedDict, closed=True):
    db_security_group: NotRequired["capo_rds.types.db_security_group.DBSecurityGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RevokeDBSecurityGroupIngressResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_security_group" in value:
        import capo_rds.types.db_security_group

        capo_rds.types.db_security_group.serialize_query(
            value["db_security_group"], pairs, f"{prefix}.DBSecurityGroup"
        )


def deserialize_query(el: Element) -> RevokeDBSecurityGroupIngressResult:
    out: RevokeDBSecurityGroupIngressResult = {}  # type: ignore[typeddict-item]
    child_db_security_group = el.find("DBSecurityGroup")
    if child_db_security_group is not None:
        import capo_rds.types.db_security_group

        out["db_security_group"] = capo_rds.types.db_security_group.deserialize_query(
            child_db_security_group
        )
    return out
