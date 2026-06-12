"""Generated from Smithy shape ``com.amazonaws.oam#GetLinkOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_oam.types.link_configuration
    import aws_sdk_oam.types.resource_types_output
    import aws_sdk_oam.types.tag_map_output


class GetLinkOutput(TypedDict):
    arn: NotRequired["str"]
    """<p>The ARN of the link.</p>"""
    id: NotRequired["str"]
    """<p>The random ID string that Amazon Web Services generated as part of the link ARN.</p>"""
    label: NotRequired["str"]
    """<p>The label that you assigned to this link, with the variables resolved to their actual values.</p>"""
    label_template: NotRequired["str"]
    """<p>The exact label template that was specified when the link was created, with the template variables not resolved.</p>"""
    resource_types: NotRequired[
        "aws_sdk_oam.types.resource_types_output.ResourceTypesOutput"
    ]
    """<p>The resource types supported by this link.</p>"""
    sink_arn: NotRequired["str"]
    """<p>The ARN of the sink that is used for this link.</p>"""
    tags: NotRequired["aws_sdk_oam.types.tag_map_output.TagMapOutput"]
    """<p>The tags assigned to the link.</p>"""
    link_configuration: NotRequired[
        "aws_sdk_oam.types.link_configuration.LinkConfiguration"
    ]
    """<p>This structure includes filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "label" in value:
        out["Label"] = value["label"]
    if "label_template" in value:
        out["LabelTemplate"] = value["label_template"]
    if "resource_types" in value:
        import aws_sdk_oam.types.resource_types_output

        out["ResourceTypes"] = aws_sdk_oam.types.resource_types_output.serialize_json(
            value["resource_types"]
        )
    if "sink_arn" in value:
        out["SinkArn"] = value["sink_arn"]
    if "tags" in value:
        import aws_sdk_oam.types.tag_map_output

        out["Tags"] = aws_sdk_oam.types.tag_map_output.serialize_json(value["tags"])
    if "link_configuration" in value:
        import aws_sdk_oam.types.link_configuration

        out["LinkConfiguration"] = aws_sdk_oam.types.link_configuration.serialize_json(
            value["link_configuration"]
        )
    return out


def deserialize_json(data: dict) -> GetLinkOutput:
    out: GetLinkOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Label" in data:
        out["label"] = data["Label"]
    if "LabelTemplate" in data:
        out["label_template"] = data["LabelTemplate"]
    if "ResourceTypes" in data:
        import aws_sdk_oam.types.resource_types_output

        out["resource_types"] = (
            aws_sdk_oam.types.resource_types_output.deserialize_json(
                data["ResourceTypes"]
            )
        )
    if "SinkArn" in data:
        out["sink_arn"] = data["SinkArn"]
    if "Tags" in data:
        import aws_sdk_oam.types.tag_map_output

        out["tags"] = aws_sdk_oam.types.tag_map_output.deserialize_json(data["Tags"])
    if "LinkConfiguration" in data:
        import aws_sdk_oam.types.link_configuration

        out["link_configuration"] = (
            aws_sdk_oam.types.link_configuration.deserialize_json(
                data["LinkConfiguration"]
            )
        )
    return out
