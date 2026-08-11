"""Generated from Smithy shape ``com.amazonaws.ec2#ClientData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.double
    import capo_ec2.types.string


class ClientData(TypedDict, closed=True):
    comment: NotRequired["capo_ec2.types.string.String"]
    """<p>A user-defined comment about the disk upload.</p>"""
    upload_end: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time that the disk upload ends.</p>"""
    upload_size: NotRequired["capo_ec2.types.double.Double"]
    """<p>The size of the uploaded disk image, in GiB.</p>"""
    upload_start: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time that the disk upload starts.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "comment" in value:
        pairs.append((f"{key_prefix}Comment", str(value["comment"])))
    if "upload_end" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["upload_end"], pairs, f"{key_prefix}UploadEnd"
        )
    if "upload_size" in value:
        pairs.append(
            (
                f"{key_prefix}UploadSize",
                (
                    "NaN"
                    if value["upload_size"] != value["upload_size"]
                    else "Infinity"
                    if value["upload_size"] == float("inf")
                    else "-Infinity"
                    if value["upload_size"] == float("-inf")
                    else str(value["upload_size"])
                ),
            )
        )
    if "upload_start" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["upload_start"], pairs, f"{key_prefix}UploadStart"
        )


def deserialize_ec2_query(el: Element) -> ClientData:
    out: ClientData = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_upload_end = el.find("UploadEnd")
    if child_upload_end is not None:
        import capo_ec2.types.date_time

        out["upload_end"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_upload_end
        )
    child_upload_size = el.find("UploadSize")
    if child_upload_size is not None:
        out["upload_size"] = float(child_upload_size.text or "")
    child_upload_start = el.find("UploadStart")
    if child_upload_start is not None:
        import capo_ec2.types.date_time

        out["upload_start"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_upload_start
        )
    return out
