"""Generated from Smithy shape ``com.amazonaws.rds#RegisterDBProxyTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.target_list


class RegisterDBProxyTargetsResponse(TypedDict, closed=True):
    db_proxy_targets: NotRequired["capo_rds.types.target_list.TargetList"]
    """<p>One or more <code>DBProxyTarget</code> objects that are created when you register targets with a target group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterDBProxyTargetsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_proxy_targets" in value:
        import capo_rds.types.target_list

        capo_rds.types.target_list.serialize_query(
            value["db_proxy_targets"], pairs, f"{key_prefix}DBProxyTargets"
        )


def deserialize_query(el: Element) -> RegisterDBProxyTargetsResponse:
    out: RegisterDBProxyTargetsResponse = {}  # type: ignore[typeddict-item]
    child_db_proxy_targets = el.find("DBProxyTargets")
    if child_db_proxy_targets is not None:
        import capo_rds.types.target_list

        out["db_proxy_targets"] = capo_rds.types.target_list.deserialize_query(
            child_db_proxy_targets
        )
    return out
