"""Generated from Smithy shape ``com.amazonaws.codecommit#TestRepositoryTriggersInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_name
    import aws_sdk_codecommit.types.repository_triggers_list


class TestRepositoryTriggersInput(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository in which to test the triggers.</p>"""
    triggers: "aws_sdk_codecommit.types.repository_triggers_list.RepositoryTriggersList"
    """<p>The list of triggers to test.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestRepositoryTriggersInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    import aws_sdk_codecommit.types.repository_triggers_list

    out["triggers"] = (
        aws_sdk_codecommit.types.repository_triggers_list.serialize_aws_json_1_1(
            value["triggers"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestRepositoryTriggersInput:
    out: TestRepositoryTriggersInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "TestRepositoryTriggersInput.repository_name required"
        )
    if "triggers" in data:
        import aws_sdk_codecommit.types.repository_triggers_list

        out["triggers"] = (
            aws_sdk_codecommit.types.repository_triggers_list.deserialize_aws_json_1_1(
                data["triggers"]
            )
        )
    else:
        raise DeserializationError("TestRepositoryTriggersInput.triggers required")
    return out
