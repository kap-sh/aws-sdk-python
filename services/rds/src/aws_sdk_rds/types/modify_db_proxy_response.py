"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBProxyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy


class ModifyDBProxyResponse(TypedDict, closed=True):
    db_proxy: NotRequired["aws_sdk_rds.types.db_proxy.DBProxy"]
    """<p>The <code>DBProxy</code> object representing the new settings for the proxy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBProxyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy" in value:
        import aws_sdk_rds.types.db_proxy

        aws_sdk_rds.types.db_proxy.serialize_query(
            value["db_proxy"], pairs, f"{prefix}.DBProxy"
        )


def deserialize_query(el: Element) -> ModifyDBProxyResponse:
    out: ModifyDBProxyResponse = {}  # type: ignore[typeddict-item]
    child_db_proxy = el.find("DBProxy")
    if child_db_proxy is not None:
        import aws_sdk_rds.types.db_proxy

        out["db_proxy"] = aws_sdk_rds.types.db_proxy.deserialize_query(child_db_proxy)
    return out
