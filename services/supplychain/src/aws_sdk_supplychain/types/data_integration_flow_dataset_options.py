"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowDatasetOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy
    import aws_sdk_supplychain.types.data_integration_flow_load_type


class DataIntegrationFlowDatasetOptions(TypedDict):
    load_type: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_load_type.DataIntegrationFlowLoadType"
    ]
    """<p>The target dataset's data load type. This only affects how source S3 files are selected in the S3-to-dataset flow.</p> <ul> <li> <p> <b>REPLACE</b> - Target dataset will get replaced with the new file added under the source s3 prefix.</p> </li> <li> <p> <b>INCREMENTAL</b> - Target dataset will get updated with the up-to-date content under S3 prefix incorporating any file additions or removals there.</p> </li> </ul>"""
    dedupe_records: NotRequired["bool"]
    """<p>The option to perform deduplication on data records sharing same primary key values. If disabled, transformed data with duplicate primary key values will ingest into dataset, for datasets within <b>asc</b> namespace, such duplicates will cause ingestion fail. If enabled without dedupeStrategy, deduplication is done by retaining a random data record among those sharing the same primary key values. If enabled with dedupeStragtegy, the deduplication is done following the strategy.</p> <p>Note that target dataset may have partition configured, when dedupe is enabled, it only dedupe against primary keys and retain only one record out of those duplicates regardless of its partition status.</p>"""
    dedupe_strategy: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy.DataIntegrationFlowDedupeStrategy"
    ]
    """<p>The deduplication strategy to dedupe the data records sharing same primary key values of the target dataset. This strategy only applies to target dataset with primary keys and with dedupeRecords option enabled. If transformed data still got duplicates after the dedupeStrategy evaluation, a random data record is chosen to be retained.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowDatasetOptions) -> dict:
    out: dict = {}
    if "load_type" in value:
        import aws_sdk_supplychain.types.data_integration_flow_load_type

        out["loadType"] = (
            aws_sdk_supplychain.types.data_integration_flow_load_type.serialize_json(
                value["load_type"]
            )
        )
    if "dedupe_records" in value:
        out["dedupeRecords"] = value["dedupe_records"]
    if "dedupe_strategy" in value:
        import aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy

        out["dedupeStrategy"] = (
            aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy.serialize_json(
                value["dedupe_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowDatasetOptions:
    out: DataIntegrationFlowDatasetOptions = {}  # type: ignore[typeddict-item]
    if "loadType" in data:
        import aws_sdk_supplychain.types.data_integration_flow_load_type

        out["load_type"] = (
            aws_sdk_supplychain.types.data_integration_flow_load_type.deserialize_json(
                data["loadType"]
            )
        )
    if "dedupeRecords" in data:
        out["dedupe_records"] = data["dedupeRecords"]
    if "dedupeStrategy" in data:
        import aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy

        out["dedupe_strategy"] = (
            aws_sdk_supplychain.types.data_integration_flow_dedupe_strategy.deserialize_json(
                data["dedupeStrategy"]
            )
        )
    return out
