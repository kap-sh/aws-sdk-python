"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryResultConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_query_output_configuration


class ProtectedQueryResultConfiguration(TypedDict, closed=True):
    output_configuration: "aws_sdk_cleanrooms.types.protected_query_output_configuration.ProtectedQueryOutputConfiguration"
    """<p>Configuration for protected query results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryResultConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.protected_query_output_configuration

    out["outputConfiguration"] = (
        aws_sdk_cleanrooms.types.protected_query_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProtectedQueryResultConfiguration:
    out: ProtectedQueryResultConfiguration = {}  # type: ignore[typeddict-item]
    if "outputConfiguration" in data:
        import aws_sdk_cleanrooms.types.protected_query_output_configuration

        out["output_configuration"] = (
            aws_sdk_cleanrooms.types.protected_query_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectedQueryResultConfiguration.output_configuration required"
        )
    return out
