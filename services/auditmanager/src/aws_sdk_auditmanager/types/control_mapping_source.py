"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlMappingSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.source_description
    import aws_sdk_auditmanager.types.source_frequency
    import aws_sdk_auditmanager.types.source_keyword
    import aws_sdk_auditmanager.types.source_name
    import aws_sdk_auditmanager.types.source_set_up_option
    import aws_sdk_auditmanager.types.source_type
    import aws_sdk_auditmanager.types.troubleshooting_text
    import aws_sdk_auditmanager.types.uuid


class ControlMappingSource(TypedDict):
    source_id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the source. </p>"""
    source_name: NotRequired["aws_sdk_auditmanager.types.source_name.SourceName"]
    """<p> The name of the source. </p>"""
    source_description: NotRequired[
        "aws_sdk_auditmanager.types.source_description.SourceDescription"
    ]
    """<p> The description of the source. </p>"""
    source_set_up_option: NotRequired[
        "aws_sdk_auditmanager.types.source_set_up_option.SourceSetUpOption"
    ]
    """<p>The setup option for the data source. This option reflects if the evidence collection method is automated or manual. If you don’t provide a value for <code>sourceSetUpOption</code>, Audit Manager automatically infers and populates the correct value based on the <code>sourceType</code> that you specify.</p>"""
    source_type: NotRequired["aws_sdk_auditmanager.types.source_type.SourceType"]
    """<p> Specifies which type of data source is used to collect evidence. </p> <ul> <li> <p>The source can be an individual data source type, such as <code>AWS_Cloudtrail</code>, <code>AWS_Config</code>, <code>AWS_Security_Hub</code>, <code>AWS_API_Call</code>, or <code>MANUAL</code>. </p> </li> <li> <p>The source can also be a managed grouping of data sources, such as a <code>Core_Control</code> or a <code>Common_Control</code>.</p> </li> </ul>"""
    source_keyword: NotRequired[
        "aws_sdk_auditmanager.types.source_keyword.SourceKeyword"
    ]
    source_frequency: NotRequired[
        "aws_sdk_auditmanager.types.source_frequency.SourceFrequency"
    ]
    """<p>Specifies how often evidence is collected from the control mapping source. </p>"""
    troubleshooting_text: NotRequired[
        "aws_sdk_auditmanager.types.troubleshooting_text.TroubleshootingText"
    ]
    """<p> The instructions for troubleshooting the control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlMappingSource) -> dict:
    out: dict = {}
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    if "source_description" in value:
        out["sourceDescription"] = value["source_description"]
    if "source_set_up_option" in value:
        import aws_sdk_auditmanager.types.source_set_up_option

        out["sourceSetUpOption"] = (
            aws_sdk_auditmanager.types.source_set_up_option.serialize_json(
                value["source_set_up_option"]
            )
        )
    if "source_type" in value:
        import aws_sdk_auditmanager.types.source_type

        out["sourceType"] = aws_sdk_auditmanager.types.source_type.serialize_json(
            value["source_type"]
        )
    if "source_keyword" in value:
        import aws_sdk_auditmanager.types.source_keyword

        out["sourceKeyword"] = aws_sdk_auditmanager.types.source_keyword.serialize_json(
            value["source_keyword"]
        )
    if "source_frequency" in value:
        import aws_sdk_auditmanager.types.source_frequency

        out["sourceFrequency"] = (
            aws_sdk_auditmanager.types.source_frequency.serialize_json(
                value["source_frequency"]
            )
        )
    if "troubleshooting_text" in value:
        out["troubleshootingText"] = value["troubleshooting_text"]
    return out


def deserialize_json(data: dict) -> ControlMappingSource:
    out: ControlMappingSource = {}  # type: ignore[typeddict-item]
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    if "sourceDescription" in data:
        out["source_description"] = data["sourceDescription"]
    if "sourceSetUpOption" in data:
        import aws_sdk_auditmanager.types.source_set_up_option

        out["source_set_up_option"] = (
            aws_sdk_auditmanager.types.source_set_up_option.deserialize_json(
                data["sourceSetUpOption"]
            )
        )
    if "sourceType" in data:
        import aws_sdk_auditmanager.types.source_type

        out["source_type"] = aws_sdk_auditmanager.types.source_type.deserialize_json(
            data["sourceType"]
        )
    if "sourceKeyword" in data:
        import aws_sdk_auditmanager.types.source_keyword

        out["source_keyword"] = (
            aws_sdk_auditmanager.types.source_keyword.deserialize_json(
                data["sourceKeyword"]
            )
        )
    if "sourceFrequency" in data:
        import aws_sdk_auditmanager.types.source_frequency

        out["source_frequency"] = (
            aws_sdk_auditmanager.types.source_frequency.deserialize_json(
                data["sourceFrequency"]
            )
        )
    if "troubleshootingText" in data:
        out["troubleshooting_text"] = data["troubleshootingText"]
    return out
