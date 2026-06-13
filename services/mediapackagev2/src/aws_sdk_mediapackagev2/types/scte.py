"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#Scte``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.custom_ad_type_list
    import aws_sdk_mediapackagev2.types.scte_filter_list
    import aws_sdk_mediapackagev2.types.scte_in_segments


class Scte(TypedDict):
    scte_filter: NotRequired[
        "aws_sdk_mediapackagev2.types.scte_filter_list.ScteFilterList"
    ]
    """<p>The SCTE-35 message types that you want to be treated as ad markers in the output.</p>"""
    scte_in_segments: NotRequired[
        "aws_sdk_mediapackagev2.types.scte_in_segments.ScteInSegments"
    ]
    """<p>Controls whether SCTE-35 messages are included in segment files.</p> <ul> <li> <p>None – SCTE-35 messages are not included in segments (default)</p> </li> <li> <p>All – SCTE-35 messages are embedded in segment data</p> </li> <li> <p>MatchesFilter – SCTE-35 messages which match the ScteFilter are embedded in segment data</p> </li> </ul> <p> For DASH manifests, when set to <code>All</code> or <code>MatchesFilter</code>, an <code>InbandEventStream</code> tag signals that SCTE messages are present in segments. This setting works independently of manifest ad markers.</p>"""
    custom_ad_types: NotRequired[
        "aws_sdk_mediapackagev2.types.custom_ad_type_list.CustomAdTypeList"
    ]
    """<p>A list of additional non-Ad SCTE-35 event types to treat as advertisements. When configured, events matching these types produce ad markers (such as <code>SCTE35-OUT</code> and <code>SCTE35-IN</code> in HLS DATERANGE tags) in manifests.</p> <p>Valid values: <code>PROGRAM</code> | <code>CHAPTER</code> | <code>UNSCHEDULED_EVENT</code> | <code>ALTERNATE_CONTENT_OPPORTUNITY</code> | <code>NETWORK</code> </p> <p>If you don't specify any values, the default is empty (only default ad types are used).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Scte) -> dict:
    out: dict = {}
    if "scte_filter" in value:
        import aws_sdk_mediapackagev2.types.scte_filter_list

        out["ScteFilter"] = (
            aws_sdk_mediapackagev2.types.scte_filter_list.serialize_json(
                value["scte_filter"]
            )
        )
    if "scte_in_segments" in value:
        import aws_sdk_mediapackagev2.types.scte_in_segments

        out["ScteInSegments"] = (
            aws_sdk_mediapackagev2.types.scte_in_segments.serialize_json(
                value["scte_in_segments"]
            )
        )
    if "custom_ad_types" in value:
        import aws_sdk_mediapackagev2.types.custom_ad_type_list

        out["CustomAdTypes"] = (
            aws_sdk_mediapackagev2.types.custom_ad_type_list.serialize_json(
                value["custom_ad_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> Scte:
    out: Scte = {}  # type: ignore[typeddict-item]
    if "ScteFilter" in data:
        import aws_sdk_mediapackagev2.types.scte_filter_list

        out["scte_filter"] = (
            aws_sdk_mediapackagev2.types.scte_filter_list.deserialize_json(
                data["ScteFilter"]
            )
        )
    if "ScteInSegments" in data:
        import aws_sdk_mediapackagev2.types.scte_in_segments

        out["scte_in_segments"] = (
            aws_sdk_mediapackagev2.types.scte_in_segments.deserialize_json(
                data["ScteInSegments"]
            )
        )
    if "CustomAdTypes" in data:
        import aws_sdk_mediapackagev2.types.custom_ad_type_list

        out["custom_ad_types"] = (
            aws_sdk_mediapackagev2.types.custom_ad_type_list.deserialize_json(
                data["CustomAdTypes"]
            )
        )
    return out
