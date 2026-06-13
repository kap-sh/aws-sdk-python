"""Generated from Smithy shape ``com.amazonaws.mwaa#ListEnvironmentsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mwaa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_list
    import aws_sdk_mwaa.types.next_token


class ListEnvironmentsOutput(TypedDict):
    environments: "aws_sdk_mwaa.types.environment_list.EnvironmentList"
    """<p>Returns a list of Amazon MWAA environments.</p>"""
    next_token: NotRequired["aws_sdk_mwaa.types.next_token.NextToken"]
    """<p>Retrieves the next page of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsOutput) -> dict:
    out: dict = {}
    import aws_sdk_mwaa.types.environment_list

    out["Environments"] = aws_sdk_mwaa.types.environment_list.serialize_json(
        value["environments"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentsOutput:
    out: ListEnvironmentsOutput = {}  # type: ignore[typeddict-item]
    if "Environments" in data:
        import aws_sdk_mwaa.types.environment_list

        out["environments"] = aws_sdk_mwaa.types.environment_list.deserialize_json(
            data["Environments"]
        )
    else:
        raise DeserializationError("ListEnvironmentsOutput.environments required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
