"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBProxyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy


class DeleteDBProxyResponse(TypedDict):
    db_proxy: NotRequired["aws_sdk_rds.types.db_proxy.DBProxy"]
    """<p>The data structure representing the details of the DB proxy that you delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBProxyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy" in value:
        import aws_sdk_rds.types.db_proxy

        aws_sdk_rds.types.db_proxy.serialize_query(
            value["db_proxy"], pairs, f"{prefix}.DBProxy"
        )


def deserialize_query(el: Element) -> DeleteDBProxyResponse:
    out: DeleteDBProxyResponse = {}  # type: ignore[typeddict-item]
    child_db_proxy = el.find("DBProxy")
    if child_db_proxy is not None:
        import aws_sdk_rds.types.db_proxy

        out["db_proxy"] = aws_sdk_rds.types.db_proxy.deserialize_query(child_db_proxy)
    return out
