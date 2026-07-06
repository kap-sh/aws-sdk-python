"""Generated from Smithy shape ``com.amazonaws.securitylake#DeleteAwsLogSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_log_source_configuration_list


class DeleteAwsLogSourceRequest(TypedDict, closed=True):
    sources: "aws_sdk_securitylake.types.aws_log_source_configuration_list.AwsLogSourceConfigurationList"
    """<p>Specify the natively-supported Amazon Web Services service to remove as a source in Security Lake.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAwsLogSourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_securitylake.types.aws_log_source_configuration_list

    out["sources"] = (
        aws_sdk_securitylake.types.aws_log_source_configuration_list.serialize_json(
            value["sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteAwsLogSourceRequest:
    out: DeleteAwsLogSourceRequest = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import aws_sdk_securitylake.types.aws_log_source_configuration_list

        out["sources"] = (
            aws_sdk_securitylake.types.aws_log_source_configuration_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("DeleteAwsLogSourceRequest.sources required")
    return out
