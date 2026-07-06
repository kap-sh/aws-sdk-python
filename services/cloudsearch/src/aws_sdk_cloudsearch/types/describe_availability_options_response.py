"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeAvailabilityOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.availability_options_status


class DescribeAvailabilityOptionsResponse(TypedDict, closed=True):
    availability_options: NotRequired[
        "aws_sdk_cloudsearch.types.availability_options_status.AvailabilityOptionsStatus"
    ]
    """<p>The availability options configured for the domain. Indicates whether Multi-AZ is enabled for the domain. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAvailabilityOptionsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "availability_options" in value:
        import aws_sdk_cloudsearch.types.availability_options_status

        aws_sdk_cloudsearch.types.availability_options_status.serialize_query(
            value["availability_options"], pairs, f"{prefix}.AvailabilityOptions"
        )


def deserialize_query(el: Element) -> DescribeAvailabilityOptionsResponse:
    out: DescribeAvailabilityOptionsResponse = {}  # type: ignore[typeddict-item]
    child_availability_options = el.find("AvailabilityOptions")
    if child_availability_options is not None:
        import aws_sdk_cloudsearch.types.availability_options_status

        out["availability_options"] = (
            aws_sdk_cloudsearch.types.availability_options_status.deserialize_query(
                child_availability_options
            )
        )
    return out
