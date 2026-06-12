"""Generated from Smithy shape ``com.amazonaws.codecommit#PutRepositoryTriggersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_triggers_configuration_id


class PutRepositoryTriggersOutput(TypedDict):
    configuration_id: NotRequired[
        "aws_sdk_codecommit.types.repository_triggers_configuration_id.RepositoryTriggersConfigurationId"
    ]
    """<p>The system-generated unique ID for the create or update operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRepositoryTriggersOutput) -> dict:
    out: dict = {}
    if "configuration_id" in value:
        out["configurationId"] = value["configuration_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRepositoryTriggersOutput:
    out: PutRepositoryTriggersOutput = {}  # type: ignore[typeddict-item]
    if "configurationId" in data:
        out["configuration_id"] = data["configurationId"]
    return out
