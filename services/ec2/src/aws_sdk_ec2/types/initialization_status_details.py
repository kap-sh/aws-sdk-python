"""Generated from Smithy shape ``com.amazonaws.ec2#InitializationStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.initialization_type
    import aws_sdk_ec2.types.long


class InitializationStatusDetails(TypedDict, closed=True):
    initialization_type: NotRequired[
        "aws_sdk_ec2.types.initialization_type.InitializationType"
    ]
    """<p>The method used for volume initialization. Possible values include:</p> <ul> <li> <p> <code>default</code> - Volume initialized using the default volume initialization rate or fast snapshot restore.</p> </li> <li> <p> <code>provisioned-rate</code> - Volume initialized using an Amazon EBS Provisioned Rate for Volume Initialization.</p> </li> <li> <p> <code>volume-copy</code> - Volume copy initialized at the rate for volume copies.</p> </li> </ul>"""
    progress: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The current volume initialization progress as a percentage (0-100). Returns <code>100</code> when volume initialization has completed.</p>"""
    estimated_time_to_complete_in_seconds: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The estimated remaining time, in seconds, for volume initialization to complete. Returns <code>0</code> when volume initialization has completed.</p> <p>Only available for volumes created with Amazon EBS Provisioned Rate for Volume Initialization.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InitializationStatusDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "initialization_type" in value:
        import aws_sdk_ec2.types.initialization_type

        aws_sdk_ec2.types.initialization_type.serialize_ec2_query(
            value["initialization_type"], pairs, f"{prefix}.InitializationType"
        )
    if "progress" in value:
        pairs.append((f"{prefix}.Progress", str(value["progress"])))
    if "estimated_time_to_complete_in_seconds" in value:
        pairs.append(
            (
                f"{prefix}.EstimatedTimeToCompleteInSeconds",
                str(value["estimated_time_to_complete_in_seconds"]),
            )
        )


def deserialize_ec2_query(el: Element) -> InitializationStatusDetails:
    out: InitializationStatusDetails = {}  # type: ignore[typeddict-item]
    child_initialization_type = el.find("InitializationType")
    if child_initialization_type is not None:
        import aws_sdk_ec2.types.initialization_type

        out["initialization_type"] = (
            aws_sdk_ec2.types.initialization_type.deserialize_ec2_query(
                child_initialization_type
            )
        )
    child_progress = el.find("Progress")
    if child_progress is not None:
        out["progress"] = int(child_progress.text or "")
    child_estimated_time_to_complete_in_seconds = el.find(
        "EstimatedTimeToCompleteInSeconds"
    )
    if child_estimated_time_to_complete_in_seconds is not None:
        out["estimated_time_to_complete_in_seconds"] = int(
            child_estimated_time_to_complete_in_seconds.text or ""
        )
    return out
