"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Processor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.add_keys
    import aws_sdk_cloudwatch_logs.types.copy_value
    import aws_sdk_cloudwatch_logs.types.csv
    import aws_sdk_cloudwatch_logs.types.date_time_converter
    import aws_sdk_cloudwatch_logs.types.delete_keys
    import aws_sdk_cloudwatch_logs.types.grok
    import aws_sdk_cloudwatch_logs.types.list_to_map
    import aws_sdk_cloudwatch_logs.types.lower_case_string
    import aws_sdk_cloudwatch_logs.types.move_keys
    import aws_sdk_cloudwatch_logs.types.parse_cloudfront
    import aws_sdk_cloudwatch_logs.types.parse_json
    import aws_sdk_cloudwatch_logs.types.parse_key_value
    import aws_sdk_cloudwatch_logs.types.parse_postgres
    import aws_sdk_cloudwatch_logs.types.parse_route53
    import aws_sdk_cloudwatch_logs.types.parse_to_ocsf
    import aws_sdk_cloudwatch_logs.types.parse_vpc
    import aws_sdk_cloudwatch_logs.types.parse_waf
    import aws_sdk_cloudwatch_logs.types.rename_keys
    import aws_sdk_cloudwatch_logs.types.split_string
    import aws_sdk_cloudwatch_logs.types.substitute_string
    import aws_sdk_cloudwatch_logs.types.trim_string
    import aws_sdk_cloudwatch_logs.types.type_converter
    import aws_sdk_cloudwatch_logs.types.upper_case_string


class Processor(TypedDict, closed=True):
    add_keys: NotRequired["aws_sdk_cloudwatch_logs.types.add_keys.AddKeys"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-addKeys\"> addKeys</a> processor in your transformer.</p>"""
    copy_value: NotRequired["aws_sdk_cloudwatch_logs.types.copy_value.CopyValue"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-copyValue\"> copyValue</a> processor in your transformer.</p>"""
    csv: NotRequired["aws_sdk_cloudwatch_logs.types.csv.CSV"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-CSV\"> CSV</a> processor in your transformer.</p>"""
    date_time_converter: NotRequired[
        "aws_sdk_cloudwatch_logs.types.date_time_converter.DateTimeConverter"
    ]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-datetimeConverter\"> datetimeConverter</a> processor in your transformer.</p>"""
    delete_keys: NotRequired["aws_sdk_cloudwatch_logs.types.delete_keys.DeleteKeys"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-deleteKeys\"> deleteKeys</a> processor in your transformer.</p>"""
    grok: NotRequired["aws_sdk_cloudwatch_logs.types.grok.Grok"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-grok\"> grok</a> processor in your transformer.</p>"""
    list_to_map: NotRequired["aws_sdk_cloudwatch_logs.types.list_to_map.ListToMap"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-listToMap\"> listToMap</a> processor in your transformer.</p>"""
    lower_case_string: NotRequired[
        "aws_sdk_cloudwatch_logs.types.lower_case_string.LowerCaseString"
    ]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-lowerCaseString\"> lowerCaseString</a> processor in your transformer.</p>"""
    move_keys: NotRequired["aws_sdk_cloudwatch_logs.types.move_keys.MoveKeys"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-moveKeys\"> moveKeys</a> processor in your transformer.</p>"""
    parse_cloudfront: NotRequired[
        "aws_sdk_cloudwatch_logs.types.parse_cloudfront.ParseCloudfront"
    ]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseCloudfront\"> parseCloudfront</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    parse_json: NotRequired["aws_sdk_cloudwatch_logs.types.parse_json.ParseJSON"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseJSON\"> parseJSON</a> processor in your transformer.</p>"""
    parse_key_value: NotRequired[
        "aws_sdk_cloudwatch_logs.types.parse_key_value.ParseKeyValue"
    ]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseKeyValue\"> parseKeyValue</a> processor in your transformer.</p>"""
    parse_route53: NotRequired[
        "aws_sdk_cloudwatch_logs.types.parse_route53.ParseRoute53"
    ]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseRoute53\"> parseRoute53</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    parse_to_ocsf: NotRequired[
        "aws_sdk_cloudwatch_logs.types.parse_to_ocsf.ParseToOCSF"
    ]
    """<p>Use this parameter to convert logs into Open Cybersecurity Schema (OCSF) format.</p>"""
    parse_postgres: NotRequired[
        "aws_sdk_cloudwatch_logs.types.parse_postgres.ParsePostgres"
    ]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parsePostGres\"> parsePostGres</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    parse_vpc: NotRequired["aws_sdk_cloudwatch_logs.types.parse_vpc.ParseVPC"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseVPC\"> parseVPC</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    parse_waf: NotRequired["aws_sdk_cloudwatch_logs.types.parse_waf.ParseWAF"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseWAF\"> parseWAF</a> processor in your transformer.</p> <p>If you use this processor, it must be the first processor in your transformer.</p>"""
    rename_keys: NotRequired["aws_sdk_cloudwatch_logs.types.rename_keys.RenameKeys"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-renameKeys\"> renameKeys</a> processor in your transformer.</p>"""
    split_string: NotRequired["aws_sdk_cloudwatch_logs.types.split_string.SplitString"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-splitString\"> splitString</a> processor in your transformer.</p>"""
    substitute_string: NotRequired[
        "aws_sdk_cloudwatch_logs.types.substitute_string.SubstituteString"
    ]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-substituteString\"> substituteString</a> processor in your transformer.</p>"""
    trim_string: NotRequired["aws_sdk_cloudwatch_logs.types.trim_string.TrimString"]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-trimString\"> trimString</a> processor in your transformer.</p>"""
    type_converter: NotRequired[
        "aws_sdk_cloudwatch_logs.types.type_converter.TypeConverter"
    ]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-typeConverter\"> typeConverter</a> processor in your transformer.</p>"""
    upper_case_string: NotRequired[
        "aws_sdk_cloudwatch_logs.types.upper_case_string.UpperCaseString"
    ]
    r"""<p>Use this parameter to include the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-upperCaseString\"> upperCaseString</a> processor in your transformer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Processor) -> dict:
    out: dict = {}
    if "add_keys" in value:
        import aws_sdk_cloudwatch_logs.types.add_keys

        out["addKeys"] = aws_sdk_cloudwatch_logs.types.add_keys.serialize_aws_json_1_1(
            value["add_keys"]
        )
    if "copy_value" in value:
        import aws_sdk_cloudwatch_logs.types.copy_value

        out["copyValue"] = (
            aws_sdk_cloudwatch_logs.types.copy_value.serialize_aws_json_1_1(
                value["copy_value"]
            )
        )
    if "csv" in value:
        import aws_sdk_cloudwatch_logs.types.csv

        out["csv"] = aws_sdk_cloudwatch_logs.types.csv.serialize_aws_json_1_1(
            value["csv"]
        )
    if "date_time_converter" in value:
        import aws_sdk_cloudwatch_logs.types.date_time_converter

        out["dateTimeConverter"] = (
            aws_sdk_cloudwatch_logs.types.date_time_converter.serialize_aws_json_1_1(
                value["date_time_converter"]
            )
        )
    if "delete_keys" in value:
        import aws_sdk_cloudwatch_logs.types.delete_keys

        out["deleteKeys"] = (
            aws_sdk_cloudwatch_logs.types.delete_keys.serialize_aws_json_1_1(
                value["delete_keys"]
            )
        )
    if "grok" in value:
        import aws_sdk_cloudwatch_logs.types.grok

        out["grok"] = aws_sdk_cloudwatch_logs.types.grok.serialize_aws_json_1_1(
            value["grok"]
        )
    if "list_to_map" in value:
        import aws_sdk_cloudwatch_logs.types.list_to_map

        out["listToMap"] = (
            aws_sdk_cloudwatch_logs.types.list_to_map.serialize_aws_json_1_1(
                value["list_to_map"]
            )
        )
    if "lower_case_string" in value:
        import aws_sdk_cloudwatch_logs.types.lower_case_string

        out["lowerCaseString"] = (
            aws_sdk_cloudwatch_logs.types.lower_case_string.serialize_aws_json_1_1(
                value["lower_case_string"]
            )
        )
    if "move_keys" in value:
        import aws_sdk_cloudwatch_logs.types.move_keys

        out["moveKeys"] = (
            aws_sdk_cloudwatch_logs.types.move_keys.serialize_aws_json_1_1(
                value["move_keys"]
            )
        )
    if "parse_cloudfront" in value:
        import aws_sdk_cloudwatch_logs.types.parse_cloudfront

        out["parseCloudfront"] = (
            aws_sdk_cloudwatch_logs.types.parse_cloudfront.serialize_aws_json_1_1(
                value["parse_cloudfront"]
            )
        )
    if "parse_json" in value:
        import aws_sdk_cloudwatch_logs.types.parse_json

        out["parseJSON"] = (
            aws_sdk_cloudwatch_logs.types.parse_json.serialize_aws_json_1_1(
                value["parse_json"]
            )
        )
    if "parse_key_value" in value:
        import aws_sdk_cloudwatch_logs.types.parse_key_value

        out["parseKeyValue"] = (
            aws_sdk_cloudwatch_logs.types.parse_key_value.serialize_aws_json_1_1(
                value["parse_key_value"]
            )
        )
    if "parse_route53" in value:
        import aws_sdk_cloudwatch_logs.types.parse_route53

        out["parseRoute53"] = (
            aws_sdk_cloudwatch_logs.types.parse_route53.serialize_aws_json_1_1(
                value["parse_route53"]
            )
        )
    if "parse_to_ocsf" in value:
        import aws_sdk_cloudwatch_logs.types.parse_to_ocsf

        out["parseToOCSF"] = (
            aws_sdk_cloudwatch_logs.types.parse_to_ocsf.serialize_aws_json_1_1(
                value["parse_to_ocsf"]
            )
        )
    if "parse_postgres" in value:
        import aws_sdk_cloudwatch_logs.types.parse_postgres

        out["parsePostgres"] = (
            aws_sdk_cloudwatch_logs.types.parse_postgres.serialize_aws_json_1_1(
                value["parse_postgres"]
            )
        )
    if "parse_vpc" in value:
        import aws_sdk_cloudwatch_logs.types.parse_vpc

        out["parseVPC"] = (
            aws_sdk_cloudwatch_logs.types.parse_vpc.serialize_aws_json_1_1(
                value["parse_vpc"]
            )
        )
    if "parse_waf" in value:
        import aws_sdk_cloudwatch_logs.types.parse_waf

        out["parseWAF"] = (
            aws_sdk_cloudwatch_logs.types.parse_waf.serialize_aws_json_1_1(
                value["parse_waf"]
            )
        )
    if "rename_keys" in value:
        import aws_sdk_cloudwatch_logs.types.rename_keys

        out["renameKeys"] = (
            aws_sdk_cloudwatch_logs.types.rename_keys.serialize_aws_json_1_1(
                value["rename_keys"]
            )
        )
    if "split_string" in value:
        import aws_sdk_cloudwatch_logs.types.split_string

        out["splitString"] = (
            aws_sdk_cloudwatch_logs.types.split_string.serialize_aws_json_1_1(
                value["split_string"]
            )
        )
    if "substitute_string" in value:
        import aws_sdk_cloudwatch_logs.types.substitute_string

        out["substituteString"] = (
            aws_sdk_cloudwatch_logs.types.substitute_string.serialize_aws_json_1_1(
                value["substitute_string"]
            )
        )
    if "trim_string" in value:
        import aws_sdk_cloudwatch_logs.types.trim_string

        out["trimString"] = (
            aws_sdk_cloudwatch_logs.types.trim_string.serialize_aws_json_1_1(
                value["trim_string"]
            )
        )
    if "type_converter" in value:
        import aws_sdk_cloudwatch_logs.types.type_converter

        out["typeConverter"] = (
            aws_sdk_cloudwatch_logs.types.type_converter.serialize_aws_json_1_1(
                value["type_converter"]
            )
        )
    if "upper_case_string" in value:
        import aws_sdk_cloudwatch_logs.types.upper_case_string

        out["upperCaseString"] = (
            aws_sdk_cloudwatch_logs.types.upper_case_string.serialize_aws_json_1_1(
                value["upper_case_string"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Processor:
    out: Processor = {}  # type: ignore[typeddict-item]
    if "addKeys" in data:
        import aws_sdk_cloudwatch_logs.types.add_keys

        out["add_keys"] = (
            aws_sdk_cloudwatch_logs.types.add_keys.deserialize_aws_json_1_1(
                data["addKeys"]
            )
        )
    if "copyValue" in data:
        import aws_sdk_cloudwatch_logs.types.copy_value

        out["copy_value"] = (
            aws_sdk_cloudwatch_logs.types.copy_value.deserialize_aws_json_1_1(
                data["copyValue"]
            )
        )
    if "csv" in data:
        import aws_sdk_cloudwatch_logs.types.csv

        out["csv"] = aws_sdk_cloudwatch_logs.types.csv.deserialize_aws_json_1_1(
            data["csv"]
        )
    if "dateTimeConverter" in data:
        import aws_sdk_cloudwatch_logs.types.date_time_converter

        out["date_time_converter"] = (
            aws_sdk_cloudwatch_logs.types.date_time_converter.deserialize_aws_json_1_1(
                data["dateTimeConverter"]
            )
        )
    if "deleteKeys" in data:
        import aws_sdk_cloudwatch_logs.types.delete_keys

        out["delete_keys"] = (
            aws_sdk_cloudwatch_logs.types.delete_keys.deserialize_aws_json_1_1(
                data["deleteKeys"]
            )
        )
    if "grok" in data:
        import aws_sdk_cloudwatch_logs.types.grok

        out["grok"] = aws_sdk_cloudwatch_logs.types.grok.deserialize_aws_json_1_1(
            data["grok"]
        )
    if "listToMap" in data:
        import aws_sdk_cloudwatch_logs.types.list_to_map

        out["list_to_map"] = (
            aws_sdk_cloudwatch_logs.types.list_to_map.deserialize_aws_json_1_1(
                data["listToMap"]
            )
        )
    if "lowerCaseString" in data:
        import aws_sdk_cloudwatch_logs.types.lower_case_string

        out["lower_case_string"] = (
            aws_sdk_cloudwatch_logs.types.lower_case_string.deserialize_aws_json_1_1(
                data["lowerCaseString"]
            )
        )
    if "moveKeys" in data:
        import aws_sdk_cloudwatch_logs.types.move_keys

        out["move_keys"] = (
            aws_sdk_cloudwatch_logs.types.move_keys.deserialize_aws_json_1_1(
                data["moveKeys"]
            )
        )
    if "parseCloudfront" in data:
        import aws_sdk_cloudwatch_logs.types.parse_cloudfront

        out["parse_cloudfront"] = (
            aws_sdk_cloudwatch_logs.types.parse_cloudfront.deserialize_aws_json_1_1(
                data["parseCloudfront"]
            )
        )
    if "parseJSON" in data:
        import aws_sdk_cloudwatch_logs.types.parse_json

        out["parse_json"] = (
            aws_sdk_cloudwatch_logs.types.parse_json.deserialize_aws_json_1_1(
                data["parseJSON"]
            )
        )
    if "parseKeyValue" in data:
        import aws_sdk_cloudwatch_logs.types.parse_key_value

        out["parse_key_value"] = (
            aws_sdk_cloudwatch_logs.types.parse_key_value.deserialize_aws_json_1_1(
                data["parseKeyValue"]
            )
        )
    if "parseRoute53" in data:
        import aws_sdk_cloudwatch_logs.types.parse_route53

        out["parse_route53"] = (
            aws_sdk_cloudwatch_logs.types.parse_route53.deserialize_aws_json_1_1(
                data["parseRoute53"]
            )
        )
    if "parseToOCSF" in data:
        import aws_sdk_cloudwatch_logs.types.parse_to_ocsf

        out["parse_to_ocsf"] = (
            aws_sdk_cloudwatch_logs.types.parse_to_ocsf.deserialize_aws_json_1_1(
                data["parseToOCSF"]
            )
        )
    if "parsePostgres" in data:
        import aws_sdk_cloudwatch_logs.types.parse_postgres

        out["parse_postgres"] = (
            aws_sdk_cloudwatch_logs.types.parse_postgres.deserialize_aws_json_1_1(
                data["parsePostgres"]
            )
        )
    if "parseVPC" in data:
        import aws_sdk_cloudwatch_logs.types.parse_vpc

        out["parse_vpc"] = (
            aws_sdk_cloudwatch_logs.types.parse_vpc.deserialize_aws_json_1_1(
                data["parseVPC"]
            )
        )
    if "parseWAF" in data:
        import aws_sdk_cloudwatch_logs.types.parse_waf

        out["parse_waf"] = (
            aws_sdk_cloudwatch_logs.types.parse_waf.deserialize_aws_json_1_1(
                data["parseWAF"]
            )
        )
    if "renameKeys" in data:
        import aws_sdk_cloudwatch_logs.types.rename_keys

        out["rename_keys"] = (
            aws_sdk_cloudwatch_logs.types.rename_keys.deserialize_aws_json_1_1(
                data["renameKeys"]
            )
        )
    if "splitString" in data:
        import aws_sdk_cloudwatch_logs.types.split_string

        out["split_string"] = (
            aws_sdk_cloudwatch_logs.types.split_string.deserialize_aws_json_1_1(
                data["splitString"]
            )
        )
    if "substituteString" in data:
        import aws_sdk_cloudwatch_logs.types.substitute_string

        out["substitute_string"] = (
            aws_sdk_cloudwatch_logs.types.substitute_string.deserialize_aws_json_1_1(
                data["substituteString"]
            )
        )
    if "trimString" in data:
        import aws_sdk_cloudwatch_logs.types.trim_string

        out["trim_string"] = (
            aws_sdk_cloudwatch_logs.types.trim_string.deserialize_aws_json_1_1(
                data["trimString"]
            )
        )
    if "typeConverter" in data:
        import aws_sdk_cloudwatch_logs.types.type_converter

        out["type_converter"] = (
            aws_sdk_cloudwatch_logs.types.type_converter.deserialize_aws_json_1_1(
                data["typeConverter"]
            )
        )
    if "upperCaseString" in data:
        import aws_sdk_cloudwatch_logs.types.upper_case_string

        out["upper_case_string"] = (
            aws_sdk_cloudwatch_logs.types.upper_case_string.deserialize_aws_json_1_1(
                data["upperCaseString"]
            )
        )
    return out
