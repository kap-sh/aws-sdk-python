"""Generated from Smithy shape ``com.amazonaws.redshift#TrackList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.maintenance_track

TrackList: TypeAlias = list["aws_sdk_redshift.types.maintenance_track.MaintenanceTrack"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrackList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.maintenance_track

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.maintenance_track.serialize_query(
            item, pairs, f"{prefix}.MaintenanceTrack.{n}"
        )


def deserialize_query(el: Element) -> TrackList:
    import aws_sdk_redshift.types.maintenance_track

    out: TrackList = []
    for child in el.findall("MaintenanceTrack"):
        out.append(aws_sdk_redshift.types.maintenance_track.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TrackList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.maintenance_track

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.maintenance_track.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TrackList:
    import aws_sdk_redshift.types.maintenance_track

    out: TrackList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.maintenance_track.deserialize_query(child))
    return out
