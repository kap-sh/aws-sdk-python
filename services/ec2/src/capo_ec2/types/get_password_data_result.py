"""Generated from Smithy shape ``com.amazonaws.ec2#GetPasswordDataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.password_data
    import capo_ec2.types.string


class GetPasswordDataResult(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Windows instance.</p>"""
    timestamp: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time the data was last updated.</p>"""
    password_data: NotRequired["capo_ec2.types.password_data.PasswordData"]
    """<p>The password of the instance. Returns an empty string if the password is not available.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetPasswordDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "timestamp" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["timestamp"], pairs, f"{prefix}.Timestamp"
        )
    if "password_data" in value:
        pairs.append((f"{prefix}.PasswordData", str(value["password_data"])))


def deserialize_ec2_query(el: Element) -> GetPasswordDataResult:
    out: GetPasswordDataResult = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_ec2.types.date_time

        out["timestamp"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_timestamp
        )
    child_password_data = el.find("PasswordData")
    if child_password_data is not None:
        out["password_data"] = str(child_password_data.text or "")
    return out
