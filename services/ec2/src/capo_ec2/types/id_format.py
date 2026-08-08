"""Generated from Smithy shape ``com.amazonaws.ec2#IdFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.string


class IdFormat(TypedDict, closed=True):
    deadline: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date in UTC at which you are permanently switched over to using longer IDs. If a deadline is not yet available for this resource type, this field is not returned.</p>"""
    resource: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of resource.</p>"""
    use_long_ids: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether longer IDs (17-character IDs) are enabled for the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IdFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "deadline" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["deadline"], pairs, f"{key_prefix}Deadline"
        )
    if "resource" in value:
        pairs.append((f"{key_prefix}Resource", str(value["resource"])))
    if "use_long_ids" in value:
        pairs.append(
            (f"{key_prefix}UseLongIds", "true" if value["use_long_ids"] else "false")
        )


def deserialize_ec2_query(el: Element) -> IdFormat:
    out: IdFormat = {}  # type: ignore[typeddict-item]
    child_deadline = el.find("deadline")
    if child_deadline is not None:
        import capo_ec2.types.date_time

        out["deadline"] = capo_ec2.types.date_time.deserialize_ec2_query(child_deadline)
    child_resource = el.find("resource")
    if child_resource is not None:
        out["resource"] = str(child_resource.text or "")
    child_use_long_ids = el.find("useLongIds")
    if child_use_long_ids is not None:
        out["use_long_ids"] = (child_use_long_ids.text or "").lower() == "true"
    return out
