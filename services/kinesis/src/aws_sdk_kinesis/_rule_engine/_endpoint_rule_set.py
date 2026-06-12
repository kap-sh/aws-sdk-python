from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    aws_parse_arn,
    get_attr,
    interpolate,
    is_valid_host_label,
    string_equals,
    substring,
)


class EndpointParams:
    def __init__(
        self,
        *,
        UseDualStack: bool | None = None,
        UseFIPS: bool | None = None,
        Region: str | None = None,
        Endpoint: str | None = None,
        StreamId: str | None = None,
        StreamARN: str | None = None,
        OperationType: str | None = None,
        ConsumerARN: str | None = None,
        ResourceARN: str | None = None,
    ):
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.StreamId = StreamId if StreamId is not None else None
        self.StreamARN = StreamARN if StreamARN is not None else None
        self.OperationType = OperationType if OperationType is not None else None
        self.ConsumerARN = ConsumerARN if ConsumerARN is not None else None
        self.ResourceARN = ResourceARN if ResourceARN is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.StreamId is not None:
        _locals["StreamIdDelimiterValue"] = substring(p.StreamId, 20, 21, False)
        if _locals["StreamIdDelimiterValue"] is not None:
            if string_equals(
                _locals["StreamIdDelimiterValue"], interpolate("-", p, _locals)
            ):
                _locals["StreamIdDelimiterReversedValue"] = substring(
                    p.StreamId, 3, 4, True
                )
                if _locals["StreamIdDelimiterReversedValue"] is not None:
                    if string_equals(
                        _locals["StreamIdDelimiterReversedValue"],
                        interpolate("-", p, _locals),
                    ):
                        _locals["StreamIdPrefixValue"] = substring(
                            p.StreamId, 0, 20, False
                        )
                        if _locals["StreamIdPrefixValue"] is not None:
                            _locals["StreamIdSuffixValue"] = substring(
                                p.StreamId, 21, 24, False
                            )
                            if _locals["StreamIdSuffixValue"] is not None:
                                if p.Region is not None:
                                    _locals["PartitionResult"] = aws_partition(p.Region)
                                    if _locals["PartitionResult"] is not None:
                                        if not (
                                            string_equals(
                                                get_attr(
                                                    _locals["PartitionResult"],
                                                    interpolate("name", p, _locals),
                                                ),
                                                interpolate("aws-iso", p, _locals),
                                            )
                                        ):
                                            if not (
                                                string_equals(
                                                    get_attr(
                                                        _locals["PartitionResult"],
                                                        interpolate("name", p, _locals),
                                                    ),
                                                    interpolate(
                                                        "aws-iso-b", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.OperationType is not None:
                                                    if p.Endpoint is not None:
                                                        _locals[
                                                            "HttpsCustomEndpointDelimiterValue"
                                                        ] = substring(
                                                            p.Endpoint, 15, 16, False
                                                        )
                                                        if (
                                                            _locals[
                                                                "HttpsCustomEndpointDelimiterValue"
                                                            ]
                                                            is not None
                                                        ):
                                                            if string_equals(
                                                                _locals[
                                                                    "HttpsCustomEndpointDelimiterValue"
                                                                ],
                                                                interpolate(
                                                                    "-", p, _locals
                                                                ),
                                                            ):
                                                                _locals[
                                                                    "HttpsEndpointDelimiterValue"
                                                                ] = substring(
                                                                    p.Endpoint,
                                                                    20,
                                                                    21,
                                                                    False,
                                                                )
                                                                if (
                                                                    _locals[
                                                                        "HttpsEndpointDelimiterValue"
                                                                    ]
                                                                    is not None
                                                                ):
                                                                    if string_equals(
                                                                        _locals[
                                                                            "HttpsEndpointDelimiterValue"
                                                                        ],
                                                                        interpolate(
                                                                            ".",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ):
                                                                        _locals[
                                                                            "HttpsCustomEndpointSuffixValue"
                                                                        ] = substring(
                                                                            p.Endpoint,
                                                                            15,
                                                                            20,
                                                                            False,
                                                                        )
                                                                        if (
                                                                            _locals[
                                                                                "HttpsCustomEndpointSuffixValue"
                                                                            ]
                                                                            is not None
                                                                        ):
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    p.UseDualStack
                                                                                    is True
                                                                                ):
                                                                                    if (
                                                                                        get_attr(
                                                                                            _locals[
                                                                                                "PartitionResult"
                                                                                            ],
                                                                                            interpolate(
                                                                                                "supportsFIPS",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        )
                                                                                        is True
                                                                                    ):
                                                                                        if (
                                                                                            get_attr(
                                                                                                _locals[
                                                                                                    "PartitionResult"
                                                                                                ],
                                                                                                interpolate(
                                                                                                    "supportsDualStack",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                            )
                                                                                            is True
                                                                                        ):
                                                                                            return Endpoint(
                                                                                                url=interpolate(
                                                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{HttpsCustomEndpointSuffixValue}-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                properties={},
                                                                                                headers={},
                                                                                            )
                                                                                        raise EndpointError(
                                                                                            interpolate(
                                                                                                "DualStack is enabled, but this partition does not support DualStack.",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        )
                                                                                    raise EndpointError(
                                                                                        interpolate(
                                                                                            "FIPS is enabled, but this partition does not support FIPS.",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    )
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsFIPS",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{HttpsCustomEndpointSuffixValue}-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        properties={},
                                                                                        headers={},
                                                                                    )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "FIPS is enabled but this partition does not support FIPS",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                )
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsDualStack",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{HttpsCustomEndpointSuffixValue}.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        properties={},
                                                                                        headers={},
                                                                                    )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "DualStack is enabled but this partition does not support DualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                )
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{HttpsCustomEndpointSuffixValue}.{Region}.{PartitionResult#dnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={},
                                                                                headers={},
                                                                            )
                                                    if p.Endpoint is not None:
                                                        _locals[
                                                            "PlainCustomEndpointDelimiterValue"
                                                        ] = substring(
                                                            p.Endpoint, 7, 8, False
                                                        )
                                                        if (
                                                            _locals[
                                                                "PlainCustomEndpointDelimiterValue"
                                                            ]
                                                            is not None
                                                        ):
                                                            if string_equals(
                                                                _locals[
                                                                    "PlainCustomEndpointDelimiterValue"
                                                                ],
                                                                interpolate(
                                                                    "-", p, _locals
                                                                ),
                                                            ):
                                                                _locals[
                                                                    "PlainEndpointDelimiterValue"
                                                                ] = substring(
                                                                    p.Endpoint,
                                                                    12,
                                                                    13,
                                                                    False,
                                                                )
                                                                if (
                                                                    _locals[
                                                                        "PlainEndpointDelimiterValue"
                                                                    ]
                                                                    is not None
                                                                ):
                                                                    if string_equals(
                                                                        _locals[
                                                                            "PlainEndpointDelimiterValue"
                                                                        ],
                                                                        interpolate(
                                                                            ".",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ):
                                                                        _locals[
                                                                            "PlainCustomEndpointSuffixValue"
                                                                        ] = substring(
                                                                            p.Endpoint,
                                                                            7,
                                                                            12,
                                                                            False,
                                                                        )
                                                                        if (
                                                                            _locals[
                                                                                "PlainCustomEndpointSuffixValue"
                                                                            ]
                                                                            is not None
                                                                        ):
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    p.UseDualStack
                                                                                    is True
                                                                                ):
                                                                                    if (
                                                                                        get_attr(
                                                                                            _locals[
                                                                                                "PartitionResult"
                                                                                            ],
                                                                                            interpolate(
                                                                                                "supportsFIPS",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        )
                                                                                        is True
                                                                                    ):
                                                                                        if (
                                                                                            get_attr(
                                                                                                _locals[
                                                                                                    "PartitionResult"
                                                                                                ],
                                                                                                interpolate(
                                                                                                    "supportsDualStack",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                            )
                                                                                            is True
                                                                                        ):
                                                                                            return Endpoint(
                                                                                                url=interpolate(
                                                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{PlainCustomEndpointSuffixValue}-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                properties={},
                                                                                                headers={},
                                                                                            )
                                                                                        raise EndpointError(
                                                                                            interpolate(
                                                                                                "DualStack is enabled, but this partition does not support DualStack.",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        )
                                                                                    raise EndpointError(
                                                                                        interpolate(
                                                                                            "FIPS is enabled, but this partition does not support FIPS.",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    )
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsFIPS",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{PlainCustomEndpointSuffixValue}-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        properties={},
                                                                                        headers={},
                                                                                    )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "FIPS is enabled but this partition does not support FIPS",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                )
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsDualStack",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{PlainCustomEndpointSuffixValue}.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        properties={},
                                                                                        headers={},
                                                                                    )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "DualStack is enabled but this partition does not support DualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                )
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{PlainCustomEndpointSuffixValue}.{Region}.{PartitionResult#dnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={},
                                                                                headers={},
                                                                            )
                                                    if p.UseFIPS is True:
                                                        if p.UseDualStack is True:
                                                            if (
                                                                get_attr(
                                                                    _locals[
                                                                        "PartitionResult"
                                                                    ],
                                                                    interpolate(
                                                                        "supportsFIPS",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                                is True
                                                            ):
                                                                if (
                                                                    get_attr(
                                                                        _locals[
                                                                            "PartitionResult"
                                                                        ],
                                                                        interpolate(
                                                                            "supportsDualStack",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    )
                                                                    is True
                                                                ):
                                                                    return Endpoint(
                                                                        url=interpolate(
                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        properties={},
                                                                        headers={},
                                                                    )
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "DualStack is enabled, but this partition does not support DualStack.",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "FIPS is enabled, but this partition does not support FIPS.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                    if p.UseFIPS is True:
                                                        if (
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "supportsFIPS",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            )
                                                            is True
                                                        ):
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                properties={},
                                                                headers={},
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "FIPS is enabled but this partition does not support FIPS",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    if p.UseDualStack is True:
                                                        if (
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "supportsDualStack",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            )
                                                            is True
                                                        ):
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                properties={},
                                                                headers={},
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "DualStack is enabled but this partition does not support DualStack",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={},
                                                        headers={},
                                                    )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Operation Type is not set. Please contact service team for resolution.",
                                                        p,
                                                        _locals,
                                                    )
                                                )
    _locals: dict[str, Any] = {}
    if p.StreamARN is not None:
        if not (p.Endpoint is not None):
            if p.Region is not None:
                _locals["PartitionResult"] = aws_partition(p.Region)
                if _locals["PartitionResult"] is not None:
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws-iso", p, _locals),
                        )
                    ):
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-iso-b", p, _locals),
                            )
                        ):
                            _locals["arn"] = aws_parse_arn(p.StreamARN)
                            if _locals["arn"] is not None:
                                if is_valid_host_label(
                                    get_attr(
                                        _locals["arn"],
                                        interpolate("accountId", p, _locals),
                                    ),
                                    False,
                                ):
                                    if is_valid_host_label(
                                        get_attr(
                                            _locals["arn"],
                                            interpolate("region", p, _locals),
                                        ),
                                        False,
                                    ):
                                        if string_equals(
                                            get_attr(
                                                _locals["arn"],
                                                interpolate("service", p, _locals),
                                            ),
                                            interpolate("kinesis", p, _locals),
                                        ):
                                            _locals["arnType"] = get_attr(
                                                _locals["arn"],
                                                interpolate(
                                                    "resourceId[0]", p, _locals
                                                ),
                                            )
                                            if _locals["arnType"] is not None:
                                                if not (
                                                    string_equals(
                                                        _locals["arnType"],
                                                        interpolate("", p, _locals),
                                                    )
                                                ):
                                                    if string_equals(
                                                        _locals["arnType"],
                                                        interpolate(
                                                            "stream", p, _locals
                                                        ),
                                                    ):
                                                        if string_equals(
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "name", p, _locals
                                                                ),
                                                            ),
                                                            interpolate(
                                                                "{arn#partition}",
                                                                p,
                                                                _locals,
                                                            ),
                                                        ):
                                                            if (
                                                                p.OperationType
                                                                is not None
                                                            ):
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        p.UseDualStack
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsFIPS",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={},
                                                                                    headers={},
                                                                                )
                                                                            raise EndpointError(
                                                                                interpolate(
                                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsFIPS",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "FIPS is enabled but this partition does not support FIPS",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                if (
                                                                    p.UseDualStack
                                                                    is True
                                                                ):
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsDualStack",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "DualStack is enabled but this partition does not support DualStack",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                return Endpoint(
                                                                    url=interpolate(
                                                                        "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={},
                                                                    headers={},
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Operation Type is not set. Please contact service team for resolution.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Partition: {arn#partition} from ARN doesn't match with partition name: {PartitionResult#name}.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: Kinesis ARNs don't support `{arnType}` arn types.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid ARN: No ARN type specified",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid ARN: The ARN was not for the Kinesis service, found: {arn#service}.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: Invalid region.", p, _locals
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Invalid account id.", p, _locals
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: Failed to parse ARN.", p, _locals
                                )
                            )
    _locals: dict[str, Any] = {}
    if p.ConsumerARN is not None:
        if not (p.Endpoint is not None):
            if p.Region is not None:
                _locals["PartitionResult"] = aws_partition(p.Region)
                if _locals["PartitionResult"] is not None:
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws-iso", p, _locals),
                        )
                    ):
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-iso-b", p, _locals),
                            )
                        ):
                            _locals["arn"] = aws_parse_arn(p.ConsumerARN)
                            if _locals["arn"] is not None:
                                if is_valid_host_label(
                                    get_attr(
                                        _locals["arn"],
                                        interpolate("accountId", p, _locals),
                                    ),
                                    False,
                                ):
                                    if is_valid_host_label(
                                        get_attr(
                                            _locals["arn"],
                                            interpolate("region", p, _locals),
                                        ),
                                        False,
                                    ):
                                        if string_equals(
                                            get_attr(
                                                _locals["arn"],
                                                interpolate("service", p, _locals),
                                            ),
                                            interpolate("kinesis", p, _locals),
                                        ):
                                            _locals["arnType"] = get_attr(
                                                _locals["arn"],
                                                interpolate(
                                                    "resourceId[0]", p, _locals
                                                ),
                                            )
                                            if _locals["arnType"] is not None:
                                                if not (
                                                    string_equals(
                                                        _locals["arnType"],
                                                        interpolate("", p, _locals),
                                                    )
                                                ):
                                                    if string_equals(
                                                        _locals["arnType"],
                                                        interpolate(
                                                            "stream", p, _locals
                                                        ),
                                                    ):
                                                        if string_equals(
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "name", p, _locals
                                                                ),
                                                            ),
                                                            interpolate(
                                                                "{arn#partition}",
                                                                p,
                                                                _locals,
                                                            ),
                                                        ):
                                                            if (
                                                                p.OperationType
                                                                is not None
                                                            ):
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        p.UseDualStack
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsFIPS",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={},
                                                                                    headers={},
                                                                                )
                                                                            raise EndpointError(
                                                                                interpolate(
                                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsFIPS",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "FIPS is enabled but this partition does not support FIPS",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                if (
                                                                    p.UseDualStack
                                                                    is True
                                                                ):
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsDualStack",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "DualStack is enabled but this partition does not support DualStack",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                return Endpoint(
                                                                    url=interpolate(
                                                                        "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={},
                                                                    headers={},
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Operation Type is not set. Please contact service team for resolution.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Partition: {arn#partition} from ARN doesn't match with partition name: {PartitionResult#name}.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: Kinesis ARNs don't support `{arnType}` arn types.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid ARN: No ARN type specified",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid ARN: The ARN was not for the Kinesis service, found: {arn#service}.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: Invalid region.", p, _locals
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Invalid account id.", p, _locals
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: Failed to parse ARN.", p, _locals
                                )
                            )
    _locals: dict[str, Any] = {}
    if p.ResourceARN is not None:
        if not (p.Endpoint is not None):
            if p.Region is not None:
                _locals["PartitionResult"] = aws_partition(p.Region)
                if _locals["PartitionResult"] is not None:
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws-iso", p, _locals),
                        )
                    ):
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-iso-b", p, _locals),
                            )
                        ):
                            _locals["arn"] = aws_parse_arn(p.ResourceARN)
                            if _locals["arn"] is not None:
                                if is_valid_host_label(
                                    get_attr(
                                        _locals["arn"],
                                        interpolate("accountId", p, _locals),
                                    ),
                                    False,
                                ):
                                    if is_valid_host_label(
                                        get_attr(
                                            _locals["arn"],
                                            interpolate("region", p, _locals),
                                        ),
                                        False,
                                    ):
                                        if string_equals(
                                            get_attr(
                                                _locals["arn"],
                                                interpolate("service", p, _locals),
                                            ),
                                            interpolate("kinesis", p, _locals),
                                        ):
                                            _locals["arnType"] = get_attr(
                                                _locals["arn"],
                                                interpolate(
                                                    "resourceId[0]", p, _locals
                                                ),
                                            )
                                            if _locals["arnType"] is not None:
                                                if not (
                                                    string_equals(
                                                        _locals["arnType"],
                                                        interpolate("", p, _locals),
                                                    )
                                                ):
                                                    if string_equals(
                                                        _locals["arnType"],
                                                        interpolate(
                                                            "stream", p, _locals
                                                        ),
                                                    ):
                                                        if string_equals(
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "name", p, _locals
                                                                ),
                                                            ),
                                                            interpolate(
                                                                "{arn#partition}",
                                                                p,
                                                                _locals,
                                                            ),
                                                        ):
                                                            if (
                                                                p.OperationType
                                                                is not None
                                                            ):
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        p.UseDualStack
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsFIPS",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={},
                                                                                    headers={},
                                                                                )
                                                                            raise EndpointError(
                                                                                interpolate(
                                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsFIPS",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "FIPS is enabled but this partition does not support FIPS",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                if (
                                                                    p.UseDualStack
                                                                    is True
                                                                ):
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsDualStack",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "DualStack is enabled but this partition does not support DualStack",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                return Endpoint(
                                                                    url=interpolate(
                                                                        "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={},
                                                                    headers={},
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Operation Type is not set. Please contact service team for resolution.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Partition: {arn#partition} from ARN doesn't match with partition name: {PartitionResult#name}.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: Kinesis ARNs don't support `{arnType}` arn types.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid ARN: No ARN type specified",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid ARN: The ARN was not for the Kinesis service, found: {arn#service}.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: Invalid region.", p, _locals
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Invalid account id.", p, _locals
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: Failed to parse ARN.", p, _locals
                                )
                            )
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        if p.UseFIPS is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: FIPS and custom endpoint are not supported",
                    p,
                    _locals,
                )
            )
        if p.UseDualStack is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: Dualstack and custom endpoint are not supported",
                    p,
                    _locals,
                )
            )
        return Endpoint(url=p.Endpoint, properties={}, headers={})
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        _locals["PartitionResult"] = aws_partition(p.Region)
        if _locals["PartitionResult"] is not None:
            if p.UseFIPS is True:
                if p.UseDualStack is True:
                    if True is get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsFIPS", p, _locals),
                    ):
                        if True is get_attr(
                            _locals["PartitionResult"],
                            interpolate("supportsDualStack", p, _locals),
                        ):
                            return Endpoint(
                                url=interpolate(
                                    "https://kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={},
                                headers={},
                            )
                    raise EndpointError(
                        interpolate(
                            "FIPS and DualStack are enabled, but this partition does not support one or both",
                            p,
                            _locals,
                        )
                    )
            if p.UseFIPS is True:
                if (
                    get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsFIPS", p, _locals),
                    )
                    is True
                ):
                    if string_equals(
                        get_attr(
                            _locals["PartitionResult"], interpolate("name", p, _locals)
                        ),
                        interpolate("aws-us-gov", p, _locals),
                    ):
                        return Endpoint(
                            url=interpolate(
                                "https://kinesis.{Region}.amazonaws.com", p, _locals
                            ),
                            properties={},
                            headers={},
                        )
                    return Endpoint(
                        url=interpolate(
                            "https://kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={},
                        headers={},
                    )
                raise EndpointError(
                    interpolate(
                        "FIPS is enabled but this partition does not support FIPS",
                        p,
                        _locals,
                    )
                )
            if p.UseDualStack is True:
                if True is get_attr(
                    _locals["PartitionResult"],
                    interpolate("supportsDualStack", p, _locals),
                ):
                    return Endpoint(
                        url=interpolate(
                            "https://kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={},
                        headers={},
                    )
                raise EndpointError(
                    interpolate(
                        "DualStack is enabled but this partition does not support DualStack",
                        p,
                        _locals,
                    )
                )
            return Endpoint(
                url=interpolate(
                    "https://kinesis.{Region}.{PartitionResult#dnsSuffix}", p, _locals
                ),
                properties={},
                headers={},
            )
    _locals: dict[str, Any] = {}
    raise EndpointError(
        interpolate("Invalid Configuration: Missing Region", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
