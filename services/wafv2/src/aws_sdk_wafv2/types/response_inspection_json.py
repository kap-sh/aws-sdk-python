"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionJson``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.field_identifier
    import aws_sdk_wafv2.types.response_inspection_json_failure_values
    import aws_sdk_wafv2.types.response_inspection_json_success_values


class ResponseInspectionJson(TypedDict):
    identifier: "aws_sdk_wafv2.types.field_identifier.FieldIdentifier"
    r"""<p>The identifier for the value to match against in the JSON. The identifier must be an exact match, including case.</p> <p>JSON examples: <code>\"Identifier\": [ \"/login/success\" ]</code> and <code>\"Identifier\": [ \"/sign-up/success\" ]</code> </p>"""
    success_values: "aws_sdk_wafv2.types.response_inspection_json_success_values.ResponseInspectionJsonSuccessValues"
    r"""<p>Values for the specified identifier in the response JSON that indicate a successful login or account creation attempt. To be counted as a success, the value must be an exact match, including case. Each value must be unique among the success and failure values. </p> <p>JSON example: <code>\"SuccessValues\": [ \"True\", \"Succeeded\" ]</code> </p>"""
    failure_values: "aws_sdk_wafv2.types.response_inspection_json_failure_values.ResponseInspectionJsonFailureValues"
    r"""<p>Values for the specified identifier in the response JSON that indicate a failed login or account creation attempt. To be counted as a failure, the value must be an exact match, including case. Each value must be unique among the success and failure values. </p> <p>JSON example: <code>\"FailureValues\": [ \"False\", \"Failed\" ]</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionJson) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    import aws_sdk_wafv2.types.response_inspection_json_success_values

    out["SuccessValues"] = (
        aws_sdk_wafv2.types.response_inspection_json_success_values.serialize_aws_json_1_1(
            value["success_values"]
        )
    )
    import aws_sdk_wafv2.types.response_inspection_json_failure_values

    out["FailureValues"] = (
        aws_sdk_wafv2.types.response_inspection_json_failure_values.serialize_aws_json_1_1(
            value["failure_values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseInspectionJson:
    out: ResponseInspectionJson = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("ResponseInspectionJson.identifier required")
    if "SuccessValues" in data:
        import aws_sdk_wafv2.types.response_inspection_json_success_values

        out["success_values"] = (
            aws_sdk_wafv2.types.response_inspection_json_success_values.deserialize_aws_json_1_1(
                data["SuccessValues"]
            )
        )
    else:
        raise DeserializationError("ResponseInspectionJson.success_values required")
    if "FailureValues" in data:
        import aws_sdk_wafv2.types.response_inspection_json_failure_values

        out["failure_values"] = (
            aws_sdk_wafv2.types.response_inspection_json_failure_values.deserialize_aws_json_1_1(
                data["FailureValues"]
            )
        )
    else:
        raise DeserializationError("ResponseInspectionJson.failure_values required")
    return out
