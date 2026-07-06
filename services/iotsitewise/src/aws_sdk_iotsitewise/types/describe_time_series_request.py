"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeTimeSeriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.custom_id
    import aws_sdk_iotsitewise.types.property_alias


class DescribeTimeSeriesRequest(TypedDict, closed=True):
    alias: NotRequired["aws_sdk_iotsitewise.types.property_alias.PropertyAlias"]
    """<p>The alias that identifies the time series.</p>"""
    asset_id: NotRequired["aws_sdk_iotsitewise.types.custom_id.CustomID"]
    r"""<p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    property_id: NotRequired["aws_sdk_iotsitewise.types.custom_id.CustomID"]
    r"""<p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references\">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTimeSeriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTimeSeriesRequest:
    out: DescribeTimeSeriesRequest = {}  # type: ignore[typeddict-item]
    return out
