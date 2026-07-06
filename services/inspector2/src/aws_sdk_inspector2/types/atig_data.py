"""Generated from Smithy shape ``com.amazonaws.inspector2#AtigData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.first_seen
    import aws_sdk_inspector2.types.last_seen
    import aws_sdk_inspector2.types.targets
    import aws_sdk_inspector2.types.ttps


class AtigData(TypedDict, closed=True):
    first_seen: NotRequired["aws_sdk_inspector2.types.first_seen.FirstSeen"]
    """<p>The date and time this vulnerability was first observed.</p>"""
    last_seen: NotRequired["aws_sdk_inspector2.types.last_seen.LastSeen"]
    """<p>The date and time this vulnerability was last observed.</p>"""
    targets: NotRequired["aws_sdk_inspector2.types.targets.Targets"]
    """<p>The commercial sectors this vulnerability targets.</p>"""
    ttps: NotRequired["aws_sdk_inspector2.types.ttps.Ttps"]
    r"""<p>The <a href=\"https://attack.mitre.org/\">MITRE ATT&amp;CK</a> tactics, techniques, and procedures (TTPs) associated with vulnerability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AtigData) -> dict:
    out: dict = {}
    if "first_seen" in value:
        import aws_sdk_inspector2.types.first_seen

        out["firstSeen"] = aws_sdk_inspector2.types.first_seen.serialize_json(
            value["first_seen"]
        )
    if "last_seen" in value:
        import aws_sdk_inspector2.types.last_seen

        out["lastSeen"] = aws_sdk_inspector2.types.last_seen.serialize_json(
            value["last_seen"]
        )
    if "targets" in value:
        import aws_sdk_inspector2.types.targets

        out["targets"] = aws_sdk_inspector2.types.targets.serialize_json(
            value["targets"]
        )
    if "ttps" in value:
        import aws_sdk_inspector2.types.ttps

        out["ttps"] = aws_sdk_inspector2.types.ttps.serialize_json(value["ttps"])
    return out


def deserialize_json(data: dict) -> AtigData:
    out: AtigData = {}  # type: ignore[typeddict-item]
    if "firstSeen" in data:
        import aws_sdk_inspector2.types.first_seen

        out["first_seen"] = aws_sdk_inspector2.types.first_seen.deserialize_json(
            data["firstSeen"]
        )
    if "lastSeen" in data:
        import aws_sdk_inspector2.types.last_seen

        out["last_seen"] = aws_sdk_inspector2.types.last_seen.deserialize_json(
            data["lastSeen"]
        )
    if "targets" in data:
        import aws_sdk_inspector2.types.targets

        out["targets"] = aws_sdk_inspector2.types.targets.deserialize_json(
            data["targets"]
        )
    if "ttps" in data:
        import aws_sdk_inspector2.types.ttps

        out["ttps"] = aws_sdk_inspector2.types.ttps.deserialize_json(data["ttps"])
    return out
