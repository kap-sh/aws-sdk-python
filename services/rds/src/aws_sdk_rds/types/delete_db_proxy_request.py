"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBProxyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy_name


class DeleteDBProxyRequest(TypedDict):
    db_proxy_name: NotRequired["aws_sdk_rds.types.db_proxy_name.DBProxyName"]
    """<p>The name of the DB proxy to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBProxyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_name" in value:
        pairs.append((f"{prefix}.DBProxyName", str(value["db_proxy_name"])))


def deserialize_query(el: Element) -> DeleteDBProxyRequest:
    out: DeleteDBProxyRequest = {}  # type: ignore[typeddict-item]
    child_db_proxy_name = el.find("DBProxyName")
    if child_db_proxy_name is not None:
        out["db_proxy_name"] = str(child_db_proxy_name.text or "")
    return out
