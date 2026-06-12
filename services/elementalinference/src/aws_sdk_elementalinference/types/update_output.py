"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.output_config
    import aws_sdk_elementalinference.types.output_status
    import aws_sdk_elementalinference.types.resource_description
    import aws_sdk_elementalinference.types.resource_name


class UpdateOutput(TypedDict):
    name: "aws_sdk_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the output.</p>"""
    output_config: "aws_sdk_elementalinference.types.output_config.OutputConfig"
    """<p>A typed property for an output in a feed. It identifies the action for Elemental Inference to perform. It also provides a repository for the results of that action. For example, CroppingConfig output will contain the metadata for the crop feature. </p>"""
    status: "aws_sdk_elementalinference.types.output_status.OutputStatus"
    """<p>The status of the output.</p>"""
    description: NotRequired[
        "aws_sdk_elementalinference.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the output.</p>"""
    from_association: NotRequired["bool"]
    """<p>Elemental Inference originally sets this parameter to True if this output was created by AssociateFeed or to False if this output was created by CreateFeed or UpdateFeed. </p> <p>You must not change this value. Therefore, use GetFeed to determine the current value. Then in the UpdateFeed request, if the current value is True, include this parameter with a value of True. If it's False, omit the parameter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_elementalinference.types.output_config

    out["outputConfig"] = aws_sdk_elementalinference.types.output_config.serialize_json(
        value["output_config"]
    )
    import aws_sdk_elementalinference.types.output_status

    out["status"] = aws_sdk_elementalinference.types.output_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "from_association" in value:
        out["fromAssociation"] = value["from_association"]
    return out


def deserialize_json(data: dict) -> UpdateOutput:
    out: UpdateOutput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateOutput.name required")
    if "outputConfig" in data:
        import aws_sdk_elementalinference.types.output_config

        out["output_config"] = (
            aws_sdk_elementalinference.types.output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    else:
        raise DeserializationError("UpdateOutput.output_config required")
    if "status" in data:
        import aws_sdk_elementalinference.types.output_status

        out["status"] = aws_sdk_elementalinference.types.output_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateOutput.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "fromAssociation" in data:
        out["from_association"] = data["fromAssociation"]
    return out
