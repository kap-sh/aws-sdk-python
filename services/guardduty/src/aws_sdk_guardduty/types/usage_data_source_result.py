"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageDataSourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.data_source
    import aws_sdk_guardduty.types.total


class UsageDataSourceResult(TypedDict, closed=True):
    data_source: NotRequired["aws_sdk_guardduty.types.data_source.DataSource"]
    """<p>The data source type that generated usage.</p>"""
    total: NotRequired["aws_sdk_guardduty.types.total.Total"]
    """<p>Represents the total of usage for the specified data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageDataSourceResult) -> dict:
    out: dict = {}
    if "data_source" in value:
        import aws_sdk_guardduty.types.data_source

        out["dataSource"] = aws_sdk_guardduty.types.data_source.serialize_json(
            value["data_source"]
        )
    if "total" in value:
        import aws_sdk_guardduty.types.total

        out["total"] = aws_sdk_guardduty.types.total.serialize_json(value["total"])
    return out


def deserialize_json(data: dict) -> UsageDataSourceResult:
    out: UsageDataSourceResult = {}  # type: ignore[typeddict-item]
    if "dataSource" in data:
        import aws_sdk_guardduty.types.data_source

        out["data_source"] = aws_sdk_guardduty.types.data_source.deserialize_json(
            data["dataSource"]
        )
    if "total" in data:
        import aws_sdk_guardduty.types.total

        out["total"] = aws_sdk_guardduty.types.total.deserialize_json(data["total"])
    return out
