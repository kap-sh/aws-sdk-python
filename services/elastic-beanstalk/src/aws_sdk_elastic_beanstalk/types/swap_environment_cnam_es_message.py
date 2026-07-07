"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SwapEnvironmentCNAMEsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.environment_id
    import aws_sdk_elastic_beanstalk.types.environment_name


class SwapEnvironmentCNAMEsMessage(TypedDict, closed=True):
    source_environment_id: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the source environment.</p> <p> Condition: You must specify at least the <code>SourceEnvironmentID</code> or the <code>SourceEnvironmentName</code>. You may also specify both. If you specify the <code>SourceEnvironmentId</code>, you must specify the <code>DestinationEnvironmentId</code>. </p>"""
    source_environment_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the source environment.</p> <p> Condition: You must specify at least the <code>SourceEnvironmentID</code> or the <code>SourceEnvironmentName</code>. You may also specify both. If you specify the <code>SourceEnvironmentName</code>, you must specify the <code>DestinationEnvironmentName</code>. </p>"""
    destination_environment_id: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the destination environment.</p> <p> Condition: You must specify at least the <code>DestinationEnvironmentID</code> or the <code>DestinationEnvironmentName</code>. You may also specify both. You must specify the <code>SourceEnvironmentId</code> with the <code>DestinationEnvironmentId</code>. </p>"""
    destination_environment_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the destination environment.</p> <p> Condition: You must specify at least the <code>DestinationEnvironmentID</code> or the <code>DestinationEnvironmentName</code>. You may also specify both. You must specify the <code>SourceEnvironmentName</code> with the <code>DestinationEnvironmentName</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SwapEnvironmentCNAMEsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_environment_id" in value:
        pairs.append(
            (f"{prefix}.SourceEnvironmentId", str(value["source_environment_id"]))
        )
    if "source_environment_name" in value:
        pairs.append(
            (f"{prefix}.SourceEnvironmentName", str(value["source_environment_name"]))
        )
    if "destination_environment_id" in value:
        pairs.append(
            (
                f"{prefix}.DestinationEnvironmentId",
                str(value["destination_environment_id"]),
            )
        )
    if "destination_environment_name" in value:
        pairs.append(
            (
                f"{prefix}.DestinationEnvironmentName",
                str(value["destination_environment_name"]),
            )
        )


def deserialize_query(el: Element) -> SwapEnvironmentCNAMEsMessage:
    out: SwapEnvironmentCNAMEsMessage = {}  # type: ignore[typeddict-item]
    child_source_environment_id = el.find("SourceEnvironmentId")
    if child_source_environment_id is not None:
        out["source_environment_id"] = str(child_source_environment_id.text or "")
    child_source_environment_name = el.find("SourceEnvironmentName")
    if child_source_environment_name is not None:
        out["source_environment_name"] = str(child_source_environment_name.text or "")
    child_destination_environment_id = el.find("DestinationEnvironmentId")
    if child_destination_environment_id is not None:
        out["destination_environment_id"] = str(
            child_destination_environment_id.text or ""
        )
    child_destination_environment_name = el.find("DestinationEnvironmentName")
    if child_destination_environment_name is not None:
        out["destination_environment_name"] = str(
            child_destination_environment_name.text or ""
        )
    return out
