"""Generated from Smithy shape ``com.amazonaws.detective#MembershipDatasources``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_id
    import aws_sdk_detective.types.datasource_package_ingest_history
    import aws_sdk_detective.types.graph_arn


class MembershipDatasources(TypedDict):
    account_id: NotRequired["aws_sdk_detective.types.account_id.AccountId"]
    """<p>The account identifier of the Amazon Web Services account.</p>"""
    graph_arn: NotRequired["aws_sdk_detective.types.graph_arn.GraphArn"]
    """<p>The ARN of the organization behavior graph.</p>"""
    datasource_package_ingest_history: NotRequired[
        "aws_sdk_detective.types.datasource_package_ingest_history.DatasourcePackageIngestHistory"
    ]
    """<p>Details on when a data source package was added to a behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipDatasources) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "graph_arn" in value:
        out["GraphArn"] = value["graph_arn"]
    if "datasource_package_ingest_history" in value:
        import aws_sdk_detective.types.datasource_package_ingest_history

        out["DatasourcePackageIngestHistory"] = (
            aws_sdk_detective.types.datasource_package_ingest_history.serialize_json(
                value["datasource_package_ingest_history"]
            )
        )
    return out


def deserialize_json(data: dict) -> MembershipDatasources:
    out: MembershipDatasources = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    if "DatasourcePackageIngestHistory" in data:
        import aws_sdk_detective.types.datasource_package_ingest_history

        out["datasource_package_ingest_history"] = (
            aws_sdk_detective.types.datasource_package_ingest_history.deserialize_json(
                data["DatasourcePackageIngestHistory"]
            )
        )
    return out
