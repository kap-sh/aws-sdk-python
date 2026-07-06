"""Generated from Smithy shape ``com.amazonaws.glue#LineageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawler_lineage_settings


class LineageConfiguration(TypedDict, closed=True):
    crawler_lineage_settings: NotRequired[
        "aws_sdk_glue.types.crawler_lineage_settings.CrawlerLineageSettings"
    ]
    """<p>Specifies whether data lineage is enabled for the crawler. Valid values are:</p> <ul> <li> <p>ENABLE: enables data lineage for the crawler</p> </li> <li> <p>DISABLE: disables data lineage for the crawler</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LineageConfiguration) -> dict:
    out: dict = {}
    if "crawler_lineage_settings" in value:
        import aws_sdk_glue.types.crawler_lineage_settings

        out["CrawlerLineageSettings"] = (
            aws_sdk_glue.types.crawler_lineage_settings.serialize_aws_json_1_1(
                value["crawler_lineage_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LineageConfiguration:
    out: LineageConfiguration = {}  # type: ignore[typeddict-item]
    if "CrawlerLineageSettings" in data:
        import aws_sdk_glue.types.crawler_lineage_settings

        out["crawler_lineage_settings"] = (
            aws_sdk_glue.types.crawler_lineage_settings.deserialize_aws_json_1_1(
                data["CrawlerLineageSettings"]
            )
        )
    return out
