"""Generated from Smithy shape ``com.amazonaws.cloudsearch#OptionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.boolean
    import aws_sdk_cloudsearch.types.option_state
    import aws_sdk_cloudsearch.types.u_int_value
    import aws_sdk_cloudsearch.types.update_timestamp


class OptionStatus(TypedDict, closed=True):
    creation_date: "aws_sdk_cloudsearch.types.update_timestamp.UpdateTimestamp"
    """<p>A timestamp for when this option was created.</p>"""
    update_date: "aws_sdk_cloudsearch.types.update_timestamp.UpdateTimestamp"
    """<p>A timestamp for when this option was last updated.</p>"""
    update_version: "aws_sdk_cloudsearch.types.u_int_value.UIntValue"
    """<p>A unique integer that indicates when this option was last updated.</p>"""
    state: "aws_sdk_cloudsearch.types.option_state.OptionState"
    """<p>The state of processing a change to an option. Possible values:</p><ul> <li><code>RequiresIndexDocuments</code>: the option's latest value will not be deployed until <a>IndexDocuments</a> has been called and indexing is complete.</li> <li><code>Processing</code>: the option's latest value is in the process of being activated. </li> <li><code>Active</code>: the option's latest value is completely deployed.</li> <li><code>FailedToValidate</code>: the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.</li> </ul>"""
    pending_deletion: NotRequired["aws_sdk_cloudsearch.types.boolean.Boolean"]
    """<p>Indicates that the option will be deleted once processing is complete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.update_timestamp

    aws_sdk_cloudsearch.types.update_timestamp.serialize_query(
        value["creation_date"], pairs, f"{prefix}.CreationDate"
    )
    import aws_sdk_cloudsearch.types.update_timestamp

    aws_sdk_cloudsearch.types.update_timestamp.serialize_query(
        value["update_date"], pairs, f"{prefix}.UpdateDate"
    )
    pairs.append((f"{prefix}.UpdateVersion", str(value.get("update_version", 0))))
    import aws_sdk_cloudsearch.types.option_state

    aws_sdk_cloudsearch.types.option_state.serialize_query(
        value["state"], pairs, f"{prefix}.State"
    )
    if "pending_deletion" in value:
        pairs.append(
            (
                f"{prefix}.PendingDeletion",
                "true" if value["pending_deletion"] else "false",
            )
        )


def deserialize_query(el: Element) -> OptionStatus:
    out: OptionStatus = {}  # type: ignore[typeddict-item]
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        import aws_sdk_cloudsearch.types.update_timestamp

        out["creation_date"] = (
            aws_sdk_cloudsearch.types.update_timestamp.deserialize_query(
                child_creation_date
            )
        )
    else:
        raise DeserializationError("OptionStatus.creation_date required")
    child_update_date = el.find("UpdateDate")
    if child_update_date is not None:
        import aws_sdk_cloudsearch.types.update_timestamp

        out["update_date"] = (
            aws_sdk_cloudsearch.types.update_timestamp.deserialize_query(
                child_update_date
            )
        )
    else:
        raise DeserializationError("OptionStatus.update_date required")
    child_update_version = el.find("UpdateVersion")
    if child_update_version is not None:
        out["update_version"] = int(child_update_version.text or "")
    else:
        out["update_version"] = 0
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_cloudsearch.types.option_state

        out["state"] = aws_sdk_cloudsearch.types.option_state.deserialize_query(
            child_state
        )
    else:
        raise DeserializationError("OptionStatus.state required")
    child_pending_deletion = el.find("PendingDeletion")
    if child_pending_deletion is not None:
        out["pending_deletion"] = (child_pending_deletion.text or "").lower() == "true"
    return out
