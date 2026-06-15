"""Generated from Smithy shape ``com.amazonaws.frauddetector#Variable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.data_source
    import aws_sdk_frauddetector.types.data_type
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.string
    import aws_sdk_frauddetector.types.time


class Variable(TypedDict):
    name: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The name of the variable.</p>"""
    data_type: NotRequired["aws_sdk_frauddetector.types.data_type.DataType"]
    r"""<p>The data type of the variable. For more information see <a href=\"https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types\">Variable types</a>.</p>"""
    data_source: NotRequired["aws_sdk_frauddetector.types.data_source.DataSource"]
    """<p>The data source of the variable.</p>"""
    default_value: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The default value of the variable.</p>"""
    description: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The description of the variable. </p>"""
    variable_type: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The variable type of the variable.</p> <p>Valid Values: <code>AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT </code> </p>"""
    last_updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The time when variable was last updated.</p>"""
    created_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>The time when the variable was created.</p>"""
    arn: NotRequired["aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The ARN of the variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Variable) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "data_type" in value:
        import aws_sdk_frauddetector.types.data_type

        out["dataType"] = aws_sdk_frauddetector.types.data_type.serialize_aws_json_1_1(
            value["data_type"]
        )
    if "data_source" in value:
        import aws_sdk_frauddetector.types.data_source

        out["dataSource"] = (
            aws_sdk_frauddetector.types.data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "description" in value:
        out["description"] = value["description"]
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Variable:
    out: Variable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "dataType" in data:
        import aws_sdk_frauddetector.types.data_type

        out["data_type"] = (
            aws_sdk_frauddetector.types.data_type.deserialize_aws_json_1_1(
                data["dataType"]
            )
        )
    if "dataSource" in data:
        import aws_sdk_frauddetector.types.data_source

        out["data_source"] = (
            aws_sdk_frauddetector.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    if "description" in data:
        out["description"] = data["description"]
    if "variableType" in data:
        out["variable_type"] = data["variableType"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
