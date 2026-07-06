"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AvailabilityOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.multi_az
    import aws_sdk_cloudsearch.types.option_status


class AvailabilityOptionsStatus(TypedDict, closed=True):
    options: "aws_sdk_cloudsearch.types.multi_az.MultiAZ"
    """<p>The availability options configured for the domain.</p>"""
    status: "aws_sdk_cloudsearch.types.option_status.OptionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityOptionsStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (f"{prefix}.Options", "true" if value.get("options", False) else "false")
    )
    import aws_sdk_cloudsearch.types.option_status

    aws_sdk_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )


def deserialize_query(el: Element) -> AvailabilityOptionsStatus:
    out: AvailabilityOptionsStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        out["options"] = (child_options.text or "").lower() == "true"
    else:
        out["options"] = False
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudsearch.types.option_status

        out["status"] = aws_sdk_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("AvailabilityOptionsStatus.status required")
    return out
