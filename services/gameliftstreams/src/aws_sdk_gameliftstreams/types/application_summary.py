"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ApplicationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_gameliftstreams.types.application_status
    import aws_sdk_gameliftstreams.types.description
    import aws_sdk_gameliftstreams.types.id
    import aws_sdk_gameliftstreams.types.identifier
    import aws_sdk_gameliftstreams.types.runtime_environment


class ApplicationSummary(TypedDict):
    arn: "aws_sdk_gameliftstreams.types.identifier.Identifier"
    """<p>An Amazon Resource Name (ARN) that's assigned to an application resource and uniquely identifies the application across all Amazon Web Services Regions. Format is <code>arn:aws:gameliftstreams:[AWS Region]:[AWS account]:application/[resource ID]</code>.</p>"""
    id: NotRequired["aws_sdk_gameliftstreams.types.id.Id"]
    """<p>An ID that uniquely identifies the application resource. Example ID: <code>a-9ZY8X7Wv6</code>. </p>"""
    description: NotRequired["aws_sdk_gameliftstreams.types.description.Description"]
    """<p>A human-readable label for the application. You can edit this value. </p>"""
    status: NotRequired[
        "aws_sdk_gameliftstreams.types.application_status.ApplicationStatus"
    ]
    """<p>The current status of the application resource. Possible statuses include the following:</p> <ul> <li> <p> <code>INITIALIZED</code>: Amazon GameLift Streams has received the request and is initiating the work flow to create an application. </p> </li> <li> <p> <code>PROCESSING</code>: The create application work flow is in process. Amazon GameLift Streams is copying the content and caching for future deployment in a stream group.</p> </li> <li> <p> <code>READY</code>: The application is ready to deploy in a stream group.</p> </li> <li> <p> <code>ERROR</code>: An error occurred when setting up the application. For more information about the error, call <code>GetApplication</code> and refer to <code>StatusReason</code>.</p> </li> <li> <p> <code>DELETING</code>: Amazon GameLift Streams is in the process of deleting the application.</p> </li> </ul>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    runtime_environment: NotRequired[
        "aws_sdk_gameliftstreams.types.runtime_environment.RuntimeEnvironment"
    ]
    """<p> Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers. </p> <p>A runtime environment can be one of the following:</p> <ul> <li> <p> For Linux applications </p> <ul> <li> <p> Ubuntu 22.04 LTS (<code>Type=UBUNTU, Version=22_04_LTS</code>) </p> </li> </ul> </li> <li> <p> For Windows applications </p> <ul> <li> <p>Microsoft Windows Server 2022 Base (<code>Type=WINDOWS, Version=2022</code>)</p> </li> <li> <p>Proton 10.0-4 (<code>Type=PROTON, Version=20260204</code>)</p> </li> <li> <p>Proton 9.0-2 (<code>Type=PROTON, Version=20250516</code>)</p> </li> <li> <p>Proton 8.0-5 (<code>Type=PROTON, Version=20241007</code>)</p> </li> <li> <p>Proton 8.0-2c (<code>Type=PROTON, Version=20230704</code>)</p> </li> </ul> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_gameliftstreams.types.application_status

        out["Status"] = aws_sdk_gameliftstreams.types.application_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import aws_sdk_gameliftstreams.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_gameliftstreams.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_gameliftstreams.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            aws_sdk_gameliftstreams.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "runtime_environment" in value:
        import aws_sdk_gameliftstreams.types.runtime_environment

        out["RuntimeEnvironment"] = (
            aws_sdk_gameliftstreams.types.runtime_environment.serialize_json(
                value["runtime_environment"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ApplicationSummary.arn required")
    if "Id" in data:
        out["id"] = data["Id"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_gameliftstreams.types.application_status

        out["status"] = (
            aws_sdk_gameliftstreams.types.application_status.deserialize_json(
                data["Status"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_gameliftstreams.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_gameliftstreams.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "RuntimeEnvironment" in data:
        import aws_sdk_gameliftstreams.types.runtime_environment

        out["runtime_environment"] = (
            aws_sdk_gameliftstreams.types.runtime_environment.deserialize_json(
                data["RuntimeEnvironment"]
            )
        )
    return out
