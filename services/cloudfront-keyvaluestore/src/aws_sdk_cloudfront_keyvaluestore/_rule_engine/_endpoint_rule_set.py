from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    aws_parse_arn,
    get_attr,
    interpolate,
    parse_url,
    string_equals,
)


class EndpointParams:
    def __init__(
        self,
        *,
        UseFIPS: bool | None = None,
        KvsARN: str | None = None,
        Region: str | None = None,
        Endpoint: str | None = None,
    ):
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.KvsARN = KvsARN if KvsARN is not None else None
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.UseFIPS is False:
        if p.KvsARN is not None:
            _locals["parsedArn"] = aws_parse_arn(p.KvsARN)
            if _locals["parsedArn"] is not None:
                if string_equals(
                    get_attr(_locals["parsedArn"], interpolate("service", p, _locals)),
                    interpolate("cloudfront", p, _locals),
                ):
                    if string_equals(
                        get_attr(
                            _locals["parsedArn"], interpolate("region", p, _locals)
                        ),
                        interpolate("", p, _locals),
                    ):
                        _locals["arnType"] = get_attr(
                            _locals["parsedArn"],
                            interpolate("resourceId[0]", p, _locals),
                        )
                        if _locals["arnType"] is not None:
                            if not (
                                string_equals(
                                    _locals["arnType"], interpolate("", p, _locals)
                                )
                            ):
                                if string_equals(
                                    _locals["arnType"],
                                    interpolate("key-value-store", p, _locals),
                                ):
                                    if string_equals(
                                        get_attr(
                                            _locals["parsedArn"],
                                            interpolate("partition", p, _locals),
                                        ),
                                        interpolate("aws", p, _locals),
                                    ):
                                        if p.Region is not None:
                                            _locals["partitionResult"] = aws_partition(
                                                p.Region
                                            )
                                            if _locals["partitionResult"] is not None:
                                                if string_equals(
                                                    get_attr(
                                                        _locals["partitionResult"],
                                                        interpolate("name", p, _locals),
                                                    ),
                                                    interpolate(
                                                        "{parsedArn#partition}",
                                                        p,
                                                        _locals,
                                                    ),
                                                ):
                                                    if p.Endpoint is not None:
                                                        _locals["url"] = parse_url(
                                                            p.Endpoint
                                                        )
                                                        if _locals["url"] is not None:
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "{url#scheme}://{parsedArn#accountId}.{url#authority}{url#path}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                properties={
                                                                    "authSchemes": [
                                                                        {
                                                                            "name": interpolate(
                                                                                "sigv4a",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingName": interpolate(
                                                                                "cloudfront-keyvaluestore",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingRegionSet": [
                                                                                interpolate(
                                                                                    "*",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            ],
                                                                        }
                                                                    ]
                                                                },
                                                                headers={},
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Provided endpoint is not a valid URL",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{parsedArn#accountId}.cloudfront-kvs.global.api.aws",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={
                                                            "authSchemes": [
                                                                {
                                                                    "name": interpolate(
                                                                        "sigv4a",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    "signingName": interpolate(
                                                                        "cloudfront-keyvaluestore",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    "signingRegionSet": [
                                                                        interpolate(
                                                                            "*",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    ],
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Client was configured for partition `{partitionResult#name}` but Kvs ARN has `{parsedArn#partition}`",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                        if p.Endpoint is not None:
                                            _locals["url"] = parse_url(p.Endpoint)
                                            if _locals["url"] is not None:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "{url#scheme}://{parsedArn#accountId}.{url#authority}{url#path}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "authSchemes": [
                                                            {
                                                                "name": interpolate(
                                                                    "sigv4a", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "cloudfront-keyvaluestore",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegionSet": [
                                                                    interpolate(
                                                                        "*", p, _locals
                                                                    )
                                                                ],
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                                            raise EndpointError(
                                                interpolate(
                                                    "Provided endpoint is not a valid URL",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        return Endpoint(
                                            url=interpolate(
                                                "https://{parsedArn#accountId}.cloudfront-kvs.global.api.aws",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "authSchemes": [
                                                    {
                                                        "name": interpolate(
                                                            "sigv4a", p, _locals
                                                        ),
                                                        "signingName": interpolate(
                                                            "cloudfront-keyvaluestore",
                                                            p,
                                                            _locals,
                                                        ),
                                                        "signingRegionSet": [
                                                            interpolate("*", p, _locals)
                                                        ],
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "CloudFront-KeyValueStore is not supported in partition `{parsedArn#partition}`",
                                            p,
                                            _locals,
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "ARN resource type is invalid. Expected `key-value-store`, found: `{arnType}`",
                                        p,
                                        _locals,
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "No resource type found in the KVS ARN. Resource type must be `key-value-store`.",
                                    p,
                                    _locals,
                                )
                            )
                        raise EndpointError(
                            interpolate(
                                "No resource type found in the KVS ARN. Resource type must be `key-value-store`.",
                                p,
                                _locals,
                            )
                        )
                    raise EndpointError(
                        interpolate(
                            "Provided ARN must be a global resource ARN. Found: `{parsedArn#region}`",
                            p,
                            _locals,
                        )
                    )
                raise EndpointError(
                    interpolate(
                        "Provided ARN is not a valid CloudFront Service ARN. Found: `{parsedArn#service}`",
                        p,
                        _locals,
                    )
                )
            raise EndpointError(interpolate("KVS ARN must be a valid ARN", p, _locals))
        raise EndpointError(
            interpolate("KVS ARN must be provided to use this service", p, _locals)
        )
    _locals: dict[str, Any] = {}
    raise EndpointError(
        interpolate(
            "Invalid Configuration: FIPS is not supported with CloudFront-KeyValueStore.",
            p,
            _locals,
        )
    )
    raise EndpointError("No endpoint rules matched")
