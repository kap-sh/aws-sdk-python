"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBProxyTargetGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy_target_group


class ModifyDBProxyTargetGroupResponse(TypedDict):
    db_proxy_target_group: NotRequired[
        "aws_sdk_rds.types.db_proxy_target_group.DBProxyTargetGroup"
    ]
    """<p>The settings of the modified <code>DBProxyTarget</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBProxyTargetGroupResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_target_group" in value:
        import aws_sdk_rds.types.db_proxy_target_group

        aws_sdk_rds.types.db_proxy_target_group.serialize_query(
            value["db_proxy_target_group"], pairs, f"{prefix}.DBProxyTargetGroup"
        )


def deserialize_query(el: Element) -> ModifyDBProxyTargetGroupResponse:
    out: ModifyDBProxyTargetGroupResponse = {}  # type: ignore[typeddict-item]
    child_db_proxy_target_group = el.find("DBProxyTargetGroup")
    if child_db_proxy_target_group is not None:
        import aws_sdk_rds.types.db_proxy_target_group

        out["db_proxy_target_group"] = (
            aws_sdk_rds.types.db_proxy_target_group.deserialize_query(
                child_db_proxy_target_group
            )
        )
    return out
