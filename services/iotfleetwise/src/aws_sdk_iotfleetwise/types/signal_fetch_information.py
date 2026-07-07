"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalFetchInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.event_expression_list
    import aws_sdk_iotfleetwise.types.language_version
    import aws_sdk_iotfleetwise.types.node_path
    import aws_sdk_iotfleetwise.types.signal_fetch_config


class SignalFetchInformation(TypedDict, closed=True):
    fully_qualified_name: "aws_sdk_iotfleetwise.types.node_path.NodePath"
    """<p>The fully qualified name of the signal to be fetched.</p>"""
    signal_fetch_config: (
        "aws_sdk_iotfleetwise.types.signal_fetch_config.SignalFetchConfig"
    )
    """<p>The configuration of the signal fetch operation.</p>"""
    condition_language_version: NotRequired[
        "aws_sdk_iotfleetwise.types.language_version.languageVersion"
    ]
    """<p>The version of the condition language used.</p>"""
    actions: "aws_sdk_iotfleetwise.types.event_expression_list.EventExpressionList"
    """<p>The actions to be performed by the signal fetch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalFetchInformation) -> dict:
    out: dict = {}
    out["fullyQualifiedName"] = value["fully_qualified_name"]
    import aws_sdk_iotfleetwise.types.signal_fetch_config

    out["signalFetchConfig"] = (
        aws_sdk_iotfleetwise.types.signal_fetch_config.serialize_aws_json_1_0(
            value["signal_fetch_config"]
        )
    )
    if "condition_language_version" in value:
        out["conditionLanguageVersion"] = value["condition_language_version"]
    import aws_sdk_iotfleetwise.types.event_expression_list

    out["actions"] = (
        aws_sdk_iotfleetwise.types.event_expression_list.serialize_aws_json_1_0(
            value["actions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SignalFetchInformation:
    out: SignalFetchInformation = {}  # type: ignore[typeddict-item]
    if "fullyQualifiedName" in data:
        out["fully_qualified_name"] = data["fullyQualifiedName"]
    else:
        raise DeserializationError(
            "SignalFetchInformation.fully_qualified_name required"
        )
    if "signalFetchConfig" in data:
        import aws_sdk_iotfleetwise.types.signal_fetch_config

        out["signal_fetch_config"] = (
            aws_sdk_iotfleetwise.types.signal_fetch_config.deserialize_aws_json_1_0(
                data["signalFetchConfig"]
            )
        )
    else:
        raise DeserializationError(
            "SignalFetchInformation.signal_fetch_config required"
        )
    if "conditionLanguageVersion" in data:
        out["condition_language_version"] = data["conditionLanguageVersion"]
    if "actions" in data:
        import aws_sdk_iotfleetwise.types.event_expression_list

        out["actions"] = (
            aws_sdk_iotfleetwise.types.event_expression_list.deserialize_aws_json_1_0(
                data["actions"]
            )
        )
    else:
        raise DeserializationError("SignalFetchInformation.actions required")
    return out
